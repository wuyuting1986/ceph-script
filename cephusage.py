from ceilometerclient import client
import datetime
import rados
import json
import pprint

Gi = 1024 * 1024 * 1024

class RadosClient(object):
    def __init__(self, cephconffile=None):
        self.cluster = rados.Rados(conffile = cephconffile)
        self.cluster.connect()

    def run_ceph_df(self):
        ret, outbuf, _outs = self.cluster.mon_command('{"prefix":"df",'
            '"format":"json"}', '')
        if ret != 0:
            print("Unable to get rados pool stats")
            raise
        return json.loads(outbuf)

    def get_pool_usage(self):
        ceph_df_out = self.run_ceph_df()
        pools_raw_status = ceph_df_out['pools']
        pool_info = {}
        for pool in pools_raw_status:
            pool_info[pool['name']] = {
                 'free_gb': pool['stats']['max_avail']/Gi,
                 'used_gb': pool['stats']['bytes_used']/Gi,
                 'used_pect': '%.2f' % (pool['stats']['bytes_used']*100.0 /
                     (pool['stats']['max_avail'] + pool['stats']['bytes_used']))}
        pprint.pprint(pool_info)
        return pool_info

    def get_cluster_usage(self):
        ceph_df_out = self.run_ceph_df()
        cluster_raw_status = ceph_df_out['stats']
        cluster_info = {
            'total_gb': cluster_raw_status['total_bytes']/Gi,
            'used_gb': cluster_raw_status['total_used_bytes']/Gi,
            'free_gb':cluster_raw_status['total_avail_bytes']/Gi,
            'used_pect': '%.2f' % (cluster_raw_status['total_used_bytes'] * 100.0 / 
                cluster_raw_status['total_bytes'])
            }
        pprint.pprint(cluster_info)
        return cluster_info

class CeiometerClient(object):
    def __init__(self, tenant_name, username, password, auth_url):
        self.os_tenant_name = tenant_name
        self.os_user_name = username
        self.os_password = password
        self.os_auth_url = auth_url

        self.client= client.get_client('2',
            os_username = self.os_user_name,
            os_password = self.os_password,
            os_tenant_name = self.os_tenant_name,
            os_auth_url = self.os_auth_url,
            os_region_name = 'langfang')

    def sample_create(self, resource_id, meter_name, meter_type, meter_unit,
                      sample_value, timestamp):
        self.client.samples.create(resource_id = resource_id,
                                   counter_name = meter_name,
                                   counter_type = meter_type,
                                   counter_unit = meter_unit,
                                   counter_volume = sample_value,
                                   timestamp = timestamp)

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT %H:%M:%S")


if __name__=='__main__':
    cephrados = RadosClient('/etc/ceph/ceph.conf')
    pools_usage = cephrados.get_pool_usage()
    cluster_usage = cephrados.get_cluster_usage()

    cclient = CeiometerClient('admin', 'admin', 'admin', 'http://192.168.1.106:35357/v2.0')
    import pdb
    pdb.set_trace()
    cclient.sample_create('esource123-1111-2222-33ee', 'ceph_util', 'gauage', 'aaaa', 35, '2015-07-24 11:01:08.827391')

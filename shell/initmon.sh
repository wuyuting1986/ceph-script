mkdir -p /var/lib/ceph/mon/ceph-storage1
ceph-mon --mkfs -i storage1 --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
/etc/init.d/ceph start mon

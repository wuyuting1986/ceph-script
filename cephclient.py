__author__ = 'wyt'

import rados
import rbd
import sys
import os

class CephRbdClient(object):
    def __init__(self, cephconf, pool, image):
        self.cephfile = cephconf
        self.pool = pool
        self.image = image

        self.cluster = rados.Rados(conffile=self.cephfile)
        self.cluster.connect()
        self.ioctx = self.cluster.open_ioctx(self.pool)
        self.image = rbd.Image(self.ioctx, self.image)

    def writedata(self, datafile):
        data = open(datafile).read()
        print "%d bytes will write into ceph" % len(data)
        try:
            self.image.write(data, 0)
        finally:
            self.image.close()

    def closeceph(self):
        self.ioctx.close()
        self.cluster.shutdown()



if  __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage:"
        print 'cephclient.py' + ' ' + 'filepath'

    filepath = sys.argv[-1]
    if not os.path.exists(filepath):
        print "File not exists"
        sys.exit(1)

    crc = CephRbdClient('/etc/ceph/ceph.conf', 'volumes', 'image1')
    crc.writedata(filepath)
    crc.writedata(filepath)
    crc.closeceph()
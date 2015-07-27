
/etc/init.d/ceph stop osd

umount  /dev/sdb1 /dev/sdc1  /dev/sdd1 /dev/sde1  /dev/sdf1  /dev/sdd2 /dev/sdc2 /dev/sdd2 /dev/sde2 /dev/sdf2
 rm -rf /var/lib/ceph/*

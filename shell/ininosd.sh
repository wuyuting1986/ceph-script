mkdir -p /var/lib/ceph/osd/ceph-0
mkdir -p /var/lib/ceph/osd/ceph-1
#mkdir -p /var/lib/ceph/osd/ceph-2
#mkdir -p /var/lib/ceph/osd/ceph-3
#mkdir -p /var/lib/ceph/osd/ceph-4

ceph-disk prepare --cluster ceph --cluster-uuid a7f64266-0894-4f1e-a635-d0aeaca0e993 --fs-type xfs  /dev/sdb1 /dev/sdb2  
ceph-disk activate /dev/sdb1
ceph-disk prepare --cluster ceph --cluster-uuid a7f64266-0894-4f1e-a635-d0aeaca0e993 --fs-type xfs  /dev/sdc1 /dev/sdc2
ceph-disk activate /dev/sdc1
#ceph-disk prepare --cluster ceph --cluster-uuid a7f64266-0894-4f1e-a635-d0aeaca0e993 --fs-type xfs  /dev/sdd1 /dev/sdd2
#ceph-disk activate /dev/sdd1
#ceph-disk prepare --cluster ceph --cluster-uuid a7f64266-0894-4f1e-a635-d0aeaca0e993 --fs-type xfs  /dev/sde1 /dev/sde2
#ceph-disk activate /dev/sde1
#ceph-disk prepare --cluster ceph --cluster-uuid a7f64266-0894-4f1e-a635-d0aeaca0e993 --fs-type xfs  /dev/sdf1 /dev/sdf2
#ceph-disk activate /dev/sdf1



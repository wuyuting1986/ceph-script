ssh computer4 ceph --admin-daemon /var/run/ceph/ceph-osd.0.asok config set $*
ssh computer4 ceph --admin-daemon /var/run/ceph/ceph-osd.2.asok config set $*

ssh computer10 ceph --admin-daemon /var/run/ceph/ceph-osd.4.asok config set $*
ssh computer10 ceph --admin-daemon /var/run/ceph/ceph-osd.6.asok config set $*
ssh computer12 ceph --admin-daemon /var/run/ceph/ceph-osd.8.asok config set $*
ssh computer12 ceph --admin-daemon /var/run/ceph/ceph-osd.10.asok config set $*
ssh computer7 ceph --admin-daemon /var/run/ceph/ceph-osd.12.asok config set $*
ssh computer7 ceph --admin-daemon /var/run/ceph/ceph-osd.14.asok config set $*
ssh computer11 ceph --admin-daemon /var/run/ceph/ceph-osd.16.asok config set $*
ssh computer11 ceph --admin-daemon /var/run/ceph/ceph-osd.18.asok config set $*
ssh computer15 ceph --admin-daemon /var/run/ceph/ceph-osd.20.asok config set $*
ssh computer15 ceph --admin-daemon /var/run/ceph/ceph-osd.22.asok config set $*
ssh computer9 ceph --admin-daemon /var/run/ceph/ceph-osd.24.asok config set $*
ssh computer9 ceph --admin-daemon /var/run/ceph/ceph-osd.26.asok config set $*
ssh computer1 ceph --admin-daemon /var/run/ceph/ceph-osd.28.asok config set $*
ssh computer1 ceph --admin-daemon /var/run/ceph/ceph-osd.30.asok config set $*


#usage
#./configall.sh osd_disk_threads 128
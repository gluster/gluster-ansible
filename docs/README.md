                         Roles for GlusterFS management

The document explains the roles available in GlusterFS project

* ctdb
* geo-replication
* nfs-ganesha
* glusterfs
  * volume_create
* system
  * backend_setup


The nfs-ganesha setup role will be explained here:

The tasks/ directory will have the following yml files which will facilitate in
deploying nfs-ganesha. Other directories like default/, files/ etc are omitted
for brevity.

tasks/
    main.yml
    prereq.yml
    post.yml

In essence this should be it. And the playbooks can be split into multiple files
depending on their length.


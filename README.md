# Gluster Ansible Roles

This repository contains [Ansible](https://www.ansible.com/) roles and playbooks to install, deploy, and configure GlusterFS.

The primary uses of the roles is to:

* Create a GlusterFS cluster (Replicate, Distributed-Replicate, Arbiter, etc).
* Configure GlusterFS usecases like NFS-Ganesha, Samba, Geo-Replication etc.
* Tear down a GlusterFS cluster.

The roles are classified into categories and reside in sub-directories under directory roles/.

Any custom modules that do not fit to Ansible upstream can be placed under modules/ directory.

To contribute to the project, refer [Contributing](CONTRIBUTING.md).

## Roles


**glusterfs**

* [peer_probe]
* [peer_detach]
* [volume_create]
* [volume_delete]

**system**

* [backend_setup]
* [backend_reset]
* [glusterfs_vg]

**cns-deploy**

*

**geo-replication**

* [georep_create]
* [georep_delete]
* [georep_pause]
* [georep_resume]
* [georep_start]
* [georep_stop]

**nfs-ganesha**

* [nfs_ganesha_create]
* [nfs_ganesha_destroy]
* [nfs_ganesha_add_node]
* [nfs_ganesha_del_node]
* [nfs_ganesha_export_vol]
* [nfs_ganesha_unexport_vol]
* [nfs_ganesha_refresh_conf]

**ctdb**

* [ctdb_setup]
* [ctdb_enable]
* [ctdb_disable]
* [ctdb_stop]
* [ctdb_start]

**quota**

* [quota_enable]
* [quota_disable]
* [quota_remove]
* [quota_remove_objects]
* [quota_default_soft_limits]
* [quota_limit_usage]
* [quota_limit_objects]
* [quota_alert_time]
* [quota_soft_timeout]
* [quota_hard_timeout]

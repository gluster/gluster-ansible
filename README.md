# Gluster Ansible Roles

This repository contains [Ansible](https://www.ansible.com/) roles and playbooks to install, deploy, and configure GlusterFS.

The primary uses of the roles is to:
* Create lvm storage
* Create a new filesystem and mount.
* Create a GlusterFS cluster with (Replicated, Distributed-Replicated, Striped, Distributed Striped) volumes.

The roles are classified into categories and reside in sub-directories under directory roles/.

To contribute to the project, refer [Contributing](CONTRIBUTING.md).

## Roles

**filesystem**


**lvm-role**


**glusterfs**

**nfs-ganesha**

* [nfs_ganesha_create]
* [nfs_ganesha_destroy]
* [nfs_ganesha_add_node]
* [nfs_ganesha_del_node]
* [nfs_ganesha_export_vol]
* [nfs_ganesha_unexport_vol]
* [nfs_ganesha_refresh_conf]

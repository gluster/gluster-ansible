# Gluster Ansible Roles

gluster-ansible project provides [Ansible](https://www.ansible.com/) roles to deploy, configure, and maintain GlusterFS clusters.

The goal of gluster-ansible is to develop roles which will enable the user to:

* subscribe to repositories which provides GlusterFS and related packages and install the packages.
* create a GlusterFS cluster (Replicate, Distributed-Replicate, Arbiter, etc).
* configure GlusterFS to enable features like NFS-Ganesha, CTDB, Geo-Replication etc.
* upgrade/downgrade the cluster
* expand/shrink the cluster

The following roles are classified into following categories, which will have sub-roles (if necessary) for specific task, which will be explained in detail in their respective repositories.

* [gluster.infra](https://github.com/gluster/gluster-ansible-infra)
* gluster.cluster
* gluster.features
* gluster.repositories
* gluster.maintenance

To contribute to the project, refer [Contributing](CONTRIBUTING.md).


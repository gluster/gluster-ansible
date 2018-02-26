glusterfs_snapshot_restore
=========

Restores the snapshot

Requirements
------------
* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------

| Name               | Required | Default Value     | Choices | Comments |

| snapname           | yes      | glustersnap       |         |  The name of the snapshot to be restored.


Dependencies
------------

None.

Example Playbook
----------------

* Creates a snapshot of the Volume

```
---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
       name: glusterfs-snapshot-restore

```
License
-------
GPLv3

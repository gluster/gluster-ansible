glusterfs_snapshot_clone
=========

Creates a clone of a snapshot. Upon successful completion, a new GlusterFS volume will be created from snapshot. The clone will be a space efficient clone, i.e, the snapshot and the clone will share the backend disk.

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------

| Name               | Required | Default Value          | Choices | Comments |

| volname            | yes      | 10.70.46.13:glustervol |         |
| clonename          | yes      | glusterclone           |         |   
| snapname           | yes      | glustersnap            |         |

Dependencies
------------

None.

Example Playbook
----------------

* Clones a snapshot

```
---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
       name: glusterfs-snapshot-clone

```
License
-------
GPLv3

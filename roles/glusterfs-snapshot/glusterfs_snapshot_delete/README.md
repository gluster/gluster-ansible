glusterfs-snapshot-delete
=========

Deletes a snapshot of a volume after deactivating it.

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------

| Name               | Required | Default Value         | Choices | Comments |

| volname            | yes      |10.70.46.13:glustervol |         | If volname is specified then all snapshots belonging to that particular volume is deleted.
| snapname           | yes      | glustersnap           |         | If snapname is specified then mentioned snapshot is deleted.  
| force              | no       | no                    | yes/no  |

Dependencies
------------

None.

Example Playbook
----------------

* Deletes a snapshot of the Volume

```
---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
       name: glusterfs-snapshot-delete

```
License
-------
GPLv3

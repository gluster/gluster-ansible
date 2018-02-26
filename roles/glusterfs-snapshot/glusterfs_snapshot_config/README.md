Role Name
=========

Changes configuration of a snapshot

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------
| Name               | Required | Default Value     | Choices        | Comments |

| snap_max_soft_limit| no       | 90%               | 1-100%         | snap-max-soft-limit are global options, that will be inherited by all volumes in the system and cannot be set to individual volumes.
| snap_max_hard_limit| no       |                   | 1-256          | Maximum hard limit for the system or the specified volume.
| activate_on_create | no       | yes               |                |
| auto_delete        | no       | disable           | enable/disable |

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
       name: glusterfs-snapshot-config

```
License
-------
GPLv3

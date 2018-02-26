glusterfs-snapshot-deactivate
=========

Deactivates the mentioned snapshot.

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------

| Name               | Required | Default Value     | Choices | Comments |

| snapname           | yes      | glustersnap       |         |
| force              | no       | no                | yes/no  |If some of the bricks of the snapshot volume are down then use the force=yes option to start them.


Dependencies
------------

None.

Example Playbook
----------------

* Deactivates a snapshot of the Volume

```
---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
       name: glusterfs-snapshot-deactivate

```
License
-------
GPLv3

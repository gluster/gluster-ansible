glusterfs-snapshot-activate
=========

Activates the mentioned snapshot.

Requirements
--------------

Ansible 2.3 and above
GlusterFS 3.x and above

Role Variables
--------------

| Name               | Required | Default Value     | Choices | Comments |

| snapname           | yes      | glustersnap       |         |Name of the snap to be activated.
| force              | no       | no                | yes/no  | If some of the bricks of the snapshot volume are down then use the force option to start them.

Dependencies
------------

None.

Example Playbook
----------------

* activates a snapshot of the Volume

```
---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
       name: glusterfs-snapshot-activate

```
License
-------
GPLv3

glusterfs-snapshot-create
=========

Creates a snapshot of a GlusterFS volume.

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------
| Name               | Required | Default Value        | Choices | Comments |

| volname            | yes      |10.70.46.13:glustervol|         |Name of the snapshot that will be created. It should be a unique name in the entire cluster.
| options            | no       | no-timestamp         |         |This is an optional field that can be used to provide a description of the snap that will be saved along with the snap.
| snapname           | yes      | glustersnap          |         |Name of the volume for which the snapshot will be created. We only support creating snapshot of single volume.
| force              | no       | no                   |         |
 Snapshot creation will fail if any brick is down. In a n-way replicated Red Hat Storage volume where n >= 3 snapshot is allowed even if some of the bricks are down. In such case quorum is checked. Quorum is checked only when the force option is provided, else by-default the snapshot create will fail if any brick is down. Refer the Overview section for more details on quorum.
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
       name: glusterfs-snapshot-create

```
License
-------
GPLv3

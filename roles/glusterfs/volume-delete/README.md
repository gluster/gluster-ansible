volume-delete
=============

Deletes a GlusterFS volume.

Requirements
------------

Ansible 2.3 and above
GlusterFS 3.x and above

Role Variables
--------------

| parameters | required | default | choices | comments |
| --- | --- | --- | --- | --- |
| force | no | | **yes** / **no** | Force option will be used while creating a volume, any warnings will be suppressed. |
| state | yes | | **present** / **absent** / **started** / **stopped** / **set** | If value is present volume will be created. If value is absent, volume will be deleted. If value is started, volume will be started. If value is stopped, volume will be stopped. |
| volname | yes | |  | Name of the volume. Refer GlusterFS documentation for valid characters in a volume name. |

Dependencies
------------

None.

Example Playbook
----------------

Deletes a GlusterFS volume

```

---
- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
      name: glusterfs/volume-delete
    vars:
        force: yes
        volname: sample_vol

```

License
-------

GPLv3


peer
====

This role will iterates through all the hosts and creates a trusted pool

Requirements
------------

* Ansible version 2.3 or higher
* GlusterFS packages

Role Variables
--------------

| Name               | Required | Default Value | Choices | Comments |
|--------------------|----------|-------------|-----------|-----------------|
| gluster_hosts      | yes   | None |              | List of ip addresses or hostnames |
| state     | yes | None | *present* / *absent* |List of VM names to be stopped before upgrade |
| force     | no | _no_ | *yes* / *no* | Valid only in case of state=absent, force a peer detach |

Dependencies
------------

None

Example Playbook
----------------

* Create a trusted storage pool.

```
---
- hosts: master
  remote_user: root
  gather_facts: no
  vars:
      gluster_hosts:
        - 10.70.43.142
        - 10.70.42.25
      state: present

  tasks:

  - include_role:
       name: ../roles/glusterfs/peer

```

Variables can go into the vars files, need not be present in the playbook

Notes
-----

While detaching a peer, i.e state=absent ensure to exclude the master from gluster_hosts.
While detaching, the glusterfs_peer module tries to detach all the hosts in the gluster_hosts list.

License
-------
GPLv3

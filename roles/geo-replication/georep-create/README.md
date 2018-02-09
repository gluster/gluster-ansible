georep-create
=============

Creates a Geo-replication session.

Requirements
------------

Ansible 2.3 and above
GlusterFS 3.x and above

Role Variables
--------------

| parameters | required | default | choices | comments |
| --- | --- | --- | --- | --- |
| state | yes | | **georep-create** / **georep-delete** / **georep-start** / **georep-stop** / **georep-resume**/ **georep-config** | Based on the state, the geo-replication sessions are created, deleted, started, stopped, paused, resumed, or configured. |
| force | no | | **yes** / **no** | Force option will be used while creating a georep session, any warnings will be suppressed. |
| gluster_hosts | yes | |  | Contains the list of hosts required to set a georep session. |
| mastervol | yes | |  | Name of the master volume. Refer GlusterFS documentation for valid characters in a volume name. |
| slavevol | yes | |  | Name of the slave volume. Refer GlusterFS documentation for valid characters in a volume name. |

Dependencies
------------

None.

Example Playbook
----------------

Create a Geo-replication session

```

---

- hosts: georep_master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
      name: geo-replication/georep-create
    vars:
        state: georep-create
        gluster_hosts:
          - 10.70.43.142
          - 10.70.42.25
        mastervol: mastervol
        slavevol: slavevol
        force: true

```

License
-------

GPLv3


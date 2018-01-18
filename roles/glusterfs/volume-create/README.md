volume-create
=============

Creates a GlusterFS volume. Volume can be of any type - replicate, distributed-replicate, arbiter ...

Requirements
------------

Ansible 2.3 and above
GlusterFS 3.x and above

Role Variables
--------------

| parameters | required | default | choices | comments |
| --- | --- | --- | --- | --- |
| arbiter_count | no | |  | Number of arbiter bricks to use (Only for arbiter volume types). |
| bricks | yes | |   | Bricks that form the GlusterFS volume. The format of the bricks would be hostname:mountpoint/brick_dir alternatively user can provide just mountpoint/birck_dir, in such a case gluster_hosts variable has to be set |
| disperse_count | | |  | Disperse count for the volume. If this value is specified, a dispersed volume will be  created |
| force | no | | **yes** / **no** | Force option will be used while creating a volume, any warnings will be suppressed. |
| gluster_hosts | yes | |  | Contains the list of hosts that have to be peer probed. |
| redundancy_count | no | |  | Specifies the number of redundant bricks while creating a disperse volume. If redundancy count is missing an optimal value is computed. |
| replica_count |  | | **2** / **3** | Replica count while creating a volume. Currently replica 2 and replica 3 are supported. |
| start | no | | **yes** / **no** | Starts the volume upon creation if start is ste to yes. |
| state | yes | | **present** / **absent** / **started** / **stopped** / **set** | If value is present volume will be created. If value is absent, volume will be deleted. If value is started, volume will be started. If value is stopped, volume will be stopped. |
| transport | no | tcp | **tcp** / **rdma** / **tcp,rdma** | The transport type for the volume. |
| volname | yes | |  | Name of the volume. Refer GlusterFS documentation for valid characters in a volume name. |

Dependencies
------------

None.

Example Playbook
----------------

Create a GlusterFS volume

```

---

- hosts: master
  remote_user: root
  gather_facts: no

  tasks:
  - include_role:
      name: glusterfs/peer
    vars:
        state: present
        gluster_hosts:
          - 10.70.43.142
          - 10.70.42.25

  - include_role:
      name: glusterfs/volume-create
    vars:
        force: yes
        gluster_hosts:
          - 10.70.43.142
          - 10.70.42.25
        bricks:
          - 10.70.43.142:/brick/rep
          - 10.70.42.25:/brick/rep
        replica: yes
        replica_count: 2
        volname: sample_vol

```

License
-------

GPLv3


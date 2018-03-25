GlusterFS
==========

Role Variables
--------------
With this role you can install glusterfs and git, install gstatus,
create gluster volume of your choice and  enable volume profile ifyou want.

The order of nodes in Distributed Replicated, Distributed Striped or Arbiter, depending on the order that they are declared in /etc/ansible/hosts

Examples of variables used in this role:
```
glusterfs_volumes:   
    - name: gv51
      stripes: 2
      bricks:
        - /mnt/bricks_striped/brick_0

or

glusterfs_volumes:   
    - name: gv52
      replicas: 2
      bricks:
        - /mnt/bricks_striped/brick_1
```

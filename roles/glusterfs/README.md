GlusterFS
==========

Role Variables
--------------
With this role you can install glusterfs and git, install gstatus,
create gluster volume of your choice and  enable volume profile ifyou want.

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

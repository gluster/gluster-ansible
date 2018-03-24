LVM
========

LVM deployment tasks for debian systems.

Role Variables

Examples of variables used in this role:
```
lvm_volume_groups:
  gluster_vg_1:
    physical_volumes:
      - /dev/vda

lvm_logical_volumes:
  glusterfs_storage:
    vg: gluster_vg_1
    size: 15G
```
Example of variables used in this role for thin-pool and thin volume respectivly
```
lvm_thin_pools:
  gluster_thin_pool:
    vg: gluster_vg_0
    size: 50G

lvm_thin_volumes:
  gluster_thin_volume:
    vg: gluster_vg_0
    thin_pool: gluster_thin_pool
    size: 20G
```

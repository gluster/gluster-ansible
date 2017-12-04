vgcreate
=========

vgcreate creates a new volume group called VolumeGroupName using the block special device PhysicalDevicePath.

Requirements
------------
If  PhysicalDevicePath  was not previously configured for LVM with pvcreate, the device will be initialized with the same default values used with pvcreate.  

Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|vgname        |yes       |         |< vgname >|Name of the volume group.|
|state         |yes       |         |**create**|create volume group.|
|disk          |yes       |         | < disk > |disk or partition on which the PV is created.|
|zero          |no        |         |**yes**/**no**|Whether or not the first 4 sectors of the device should be wiped.|
|dataalignment |no        |         |          |Align the start of the data to a multiple of this number.|
|maxlogicalvolumes|       |         |          |Sets the maximum number of logical volumes allowed in this volume group.|
|maxphysicalvolumes|      |         |          |Sets  the  maximum  number  of physical volumes that can belong to this volume group.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: vgcreate
      hosts: servers
      roles:
         - system/gluster_vg/vgcreate
```


License
-------

GNU General Public License 3.0

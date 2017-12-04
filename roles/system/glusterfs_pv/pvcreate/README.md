pvcreate
=========

pvcreate role initializes PhysicalVolume for later use by the Logical Volume Manager (LVM).

Requirements
------------
Each PhysicalVolume can be a disk partition, whole disk, meta device, or loopback file.

Role Variables
--------------

| Parameters  | Required | Default | Choices | Description |
| ----------  | -------- | ------- | ------- | ----------- |
|dataalignment|no        |         |         |Align the start of the data to a multiple of this number.|
|disk         |yes       |         |         |List of disks on which PV will be created.|
|force        |no        |         |**yes** / **no**|Force the creation without any confirmation.|
|metadatasize |no        |         |         |The approximate amount of space to be set aside for each metadata area.|
|state        |yes       |         |**present**|Create physical volume|
|uuid         |no        |         |         |Specify the UUID for the device.|
|zero         |no        |         |**y** / **n**|Whether or not to wipe the first 4 sectors (2048 bytes) of the device.|


Example Playbook
----------------

```yaml
    - name: pvcreate
      hosts: servers
      roles:
         - system/glusterfs_pv/pvcreate
```
  
License
-------

GNU General Public License 3.0

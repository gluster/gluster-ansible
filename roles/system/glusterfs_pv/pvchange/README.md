pvchange
=========

pvchange allows you to change the allocation permissions of one or more physical volumes.

Requirements
------------
Each PhysicalVolume can be a disk partition, whole disk, meta device, or loopback file.

Role Variables
--------------

| Parameters   | Required | Default | Choices | Description |
| ----------   | -------- | ------- | ------- | ----------- |
|allocatable   |no        |         |**yes** / **no** |Enable or disable allocation of physical extents on this physical volume.|
|disk          |yes       |         | < disk >|List of disks on which the PV will be changed|
|force         |no        |         |**yes** / **no**|Force the change without any confirmation.|
|metadataignore|no        |         |**yes** / **no**|Ignore or un-ignore metadata areas on this physical volume.|
|state         |yes       |         |**change**|Change physical volume.|
|uuid          |no        |         |          |Specify the UUID for the device.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: pvchange
      hosts: servers
      roles:
         - system/gluster_pv/pvchange
```
 
License
-------

GNU General Public License 3.0
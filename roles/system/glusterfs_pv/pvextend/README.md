pvextend
=========

pvextend extends PhysicalVolume which may already be in a volume group and have active logical volumes allocated on it.

Requirements
------------
Existing PhysicalVolume on the disk mentioned.

Role Variables
--------------

| Parameters  | Required | Default | Choices | Description |
| ----------  | -------- | ------- | ------- | ----------- |
|disk         |yes       |         |         |List of disks to extend PV|
|force        |no        |         |**yes** / **no**|Force the extention without any confirmation.|
|setphysicalvolumesize|no|         |         |Overrides  the automatically-detected size of the PV.|
|state        |yes       |         |**resize**|Resize physical volume|
      

Example Playbook to call the role
---------------------------------

```yaml
    - name: pvextend
      hosts: servers
      roles:
         - system/glusterfs_pv/pvextend
```

 
License
-------

GNU General Public License 3.0

pvshrink
=========

pvshrink shrinks PhysicalVolume which may already be in a volume group and have active logical volumes allocated on it.

Requirements
------------
Existing PhysicalVolume on the disk mentioned.

Role Variables
--------------

| Parameters  | Required | Default | Choices  | Description |
| ----------  | -------- | ------- | -------  | ----------- |
|disk         |yes       |         |          |List of disks to extend PV|
|setphysicalvolumesize|no|         |          |Overrides  the automatically-detected size of the PV.|
|state        |yes       |         |**resize**|Shrink physical volume|


Example Playbook to call the role
---------------------------------

```yaml
    - name: pvshrink
      hosts: servers
      roles:
         - system/glusterfs_pv/pvshrink
```

 
License
-------

GNU General Public License 3.0

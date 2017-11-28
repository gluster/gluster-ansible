pvextend
=========

pvextend extends PhysicalVolume which may already be in a volume group and have active logical volumes allocated on it.

Requirements
------------
Existing PhysicalVolume on the disk mentioned.

Role Variables
--------------
  
| Name          | Example values   | Description                           |
|---------------|------------------|---------------------------------------|
| action        | resize           | The action that needs to be performed on the pv. |
| disk          | < disk >         | disk or partition on which the pv will be extended.  |
| setphysicalvolumesize| < 1 G >   | Overrides the automatically-detected size of the PV. (Use with care, or prior to reducing the physical size of the device.) |
      

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

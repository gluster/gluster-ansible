pvcreate
=========

pvcreate role initializes PhysicalVolume for later use by the Logical Volume Manager (LVM).

Requirements
------------
Each PhysicalVolume can be a disk partition, whole disk, meta device, or loopback file.

Role Variables
--------------
    
| Name          | Example values   | Description                           |
|---------------|------------------|---------------------------------------|
| action        | create           | The action that needs to be performed on the pv. |
| disk          | < disk >         | disk or partition on which the pv will be created.  |
| force (-f)    | y                | Force  the  creation  without  any confirmation.   |
| uuid (-u)     | < uuid >         | Specify the uuid for the device.  Without this option,pvcreate generates a random uuid. |
| dataalignment (--dataalignment)  | 1280 | Align the start of the data to a multiple of this number. |
| metadatasize (--metadatasize)    | < size > | The approximate amount of space to be set aside for each metadata area. |
| zero (-Z)     | 0                | Whether or not the first 4 sectors of the device should be wiped.  |


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

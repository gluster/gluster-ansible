pvchange
=========

pvchange allows you to change the allocation permissions of one or more physical volumes.

Requirements
------------
Each PhysicalVolume can be a disk partition, whole disk, meta device, or loopback file.

Role Variables
--------------
  
| Name          | Example values   | Description                           |
|---------------|------------------|---------------------------------------|
| action        | change           | The action that needs to be performed on the pv. |
| disk          | < disk >         | disk or partition on which the pv will be changed.  |
| force (-f)    | y                | Force  the  creation  without  any confirmation.   |
| uuid (-u)     | < uuid >         | Specify the uuid for the device. Without this option,pvchange generates a random uuid. |
| allocatable   | {y|n}            | Enable or disable allocation of physical extents on this physical volume. |
| metadataignore| {y|n}            | Ignore or un-ignore metadata areas on this physical volume. |


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
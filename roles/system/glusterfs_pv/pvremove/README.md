pvremove
=========

pvremove wipes the label on a device so that LVM will no longer recognise it as a physical volume.

Requirements
------------
Existing PhysicalVolume on the disk mentioned.

Role Variables
--------------
  
| Name          | Example values   | Description                           |
|---------------|------------------|---------------------------------------|
| action        | remove           | The action that needs to be performed on the pv. |
| disk          | < disk >         | disk or partition from which the physical volume will be removed.  |
| force (-f)    | y                | Force  the  removal  without  any confirmation.   |


Example Playbook to call the role
---------------------------------

```yaml
    - name: pvremove
      hosts: servers
      roles:
         - system/glustrefs_pv/pvremove
```


License
-------

GNU General Public License 3.0

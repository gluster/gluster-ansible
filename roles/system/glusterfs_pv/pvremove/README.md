pvremove
=========

pvremove wipes the label on a device so that LVM will no longer recognise it as a physical volume.

Requirements
------------
Existing PhysicalVolume on the disk mentioned.

Role Variables
--------------

| Parameters  | Required | Default | Choices | Description |
| ----------  | -------- | ------- | ------- | ----------- |
|disk         |yes       |         |         |List of disks to remove PV|
|force        |no        |         |**yes** / **no**|Force the removal without any confirmation.|
|state        |yes       |         |**absent**|Remove physical volume|


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

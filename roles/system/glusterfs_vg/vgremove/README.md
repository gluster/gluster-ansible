vgremove
=========

vgremove allows you to remove one or more volume groups.

Requirements
------------
A volume group created on the PhysicalDevicePath.

Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|vgname        |yes       |         |< vgname >|Name of the volume group to be removed.|
|state         |yes       |         |**remove**|Remove the volume group.|
|force         |no        |         |**yes**/**no**|Force the removal of any volume group without confirmation.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: vgremove
      hosts: servers
      roles:
         - system/gluster_vg/vgremove
```


License
-------

GNU General Public License 3.0

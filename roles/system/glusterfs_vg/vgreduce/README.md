vgreduce
=========

vgreduce allows you to remove unused physical volumes from a volume group.

Requirements
------------
A volume group created on the PhysicalDevicePath.

Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|vgname        |yes       |         |< vgname >|Name of the volume group.|
|state         |yes       |         |**reduce**|Reduce the volume group.|
|disk          |yes       |         | < disk > |disk or partition on which the PV is created.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: vgreduce
      hosts: servers
      roles:
         - system/gluster_vg/vgreduce
```


License
-------

GNU General Public License 3.0

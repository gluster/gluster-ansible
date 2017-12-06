vgextend
=========

vgextend allows you to add one or more initialized physical volumes to an existing volume group to extend it in size.

Requirements
------------
A volume group created on the PhysicalDevicePath.

Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|vgname        |yes       |         |< vgname >|Name of the volume group.|
|state         |yes       |         |**extend**|extend volume group.|
|disk          |yes       |         | < disk > |disk or partition on which the PV is created.|
|zero          |no        |         |**yes**/**no**|Whether or not the first 4 sectors of the device should be wiped.|
|dataalignment |no        |         |          |Align the start of the data to a multiple of this number.|
|metadatasize  |no        |         |          |Size of metadata.|
|metadataignore|no        |         |**yes**/**no**|Enable or disable to ignore metadata.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: vgextend
      hosts: servers
      roles:
         - system/gluster_vg/vgextend
```


License
-------

GNU General Public License 3.0

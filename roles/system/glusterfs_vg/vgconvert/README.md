vgconvert
=========

vgconvert converts VolumeGroupName metadata from one format to another provided that the metadata fits into the same space.

Requirements
------------
A volume group created on the PhysicalDevicePath.

Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|vgname        |yes       |         |< vgname >|Name of the volume group.|
|metadatatype  |no        |         |< num >   |Metadata type.|
|state         |yes       |         |**convert**|convert volume group.|


Example Playbook to call the role
---------------------------------

```yaml
    - name: vgconvert
      hosts: servers
      roles:
         - system/gluster_vg/vgconvert
```


License
-------

GNU General Public License 3.0

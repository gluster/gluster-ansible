lvrename
=========

lvrename renames an existing LogicalVolume

Requirements
------------
lvrename allows you to rename a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                  |
| ----------      | -------- | ------- | -------        | -----------                  |
|lvname           |no        |         |**yes**         | Name of the LogicalVolume    |
|new_name         |no        |         |**yes**         | New name of the LogicalVolume|
|vgname           |yes       |         |**yes**         | Name of the VolumeGroup      |

Example Playbook
----------------

```yaml
    - name: lvrename
      hosts: servers
      roles:
         - system/glusterfs_lv/lvrename
```

License
-------

GNU General Public License 3.0

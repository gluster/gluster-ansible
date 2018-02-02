lvchange
========

lvchange changes certain parameters of an existing LogicalVolume

Requirements
------------
lvrename allows you to change certain parameters of a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                                         |
| ----------      | -------- | ------- | -------        | -----------                                         |
|errorwhenfull    |no        |         |**yes**/**no**  | Sets thin pool behavior when data space is exhausted|
|lvname           |no        |         |**yes**         | Name of the LogicalVolume                           |
|permission       |no        |         |**r**/**rw**    | Change access permission to read-only or read/write |
|vgname           |yes       |         |**yes**         | Name of the VolumeGroup                             |
|zero             |no        |         |**yes**/**no**  | Set zeroing mode for thin pool                      |

Example Playbook
----------------

```yaml
    - name: lvchange
      hosts: servers
      roles:
         - system/glusterfs_lv/lvchange
```

License
-------

GNU General Public License 3.0

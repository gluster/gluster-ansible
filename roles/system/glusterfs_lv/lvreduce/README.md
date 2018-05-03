lvreduce
=========

lvreduce role allows to reduce a LogicalVolume

Requirements
------------
lvreduce allows you to reduce a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                                |
| ----------      | -------- | ------- | -------        | -----------                                |
|extents          |no        |         |                |Change/set the lv size in units of extents  |
|force            |no        |         |**yes** / **no**|Force the creation without any confirmation |
|resizefs         |yes       |         |                |Resize underlying FS together with the lv   |
|size             |yes       |         |**present**     |Change/set the lv size in units of megabytes|


Example Playbook
----------------

```yaml
    - name: lvreduce
      hosts: servers
      roles:
         - system/glusterfs_lv/lvreduce
```

License
-------

GNU General Public License 3.0

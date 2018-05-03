lvextend
=========

lvextend role allows to extend a LogicalVolume

Requirements
------------
lvextend allows you to extend a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                                |
| ----------      | -------- | ------- | -------        | -----------                                |
|extents          |no        |         |                |Change/set the lv size in units of extents  |
|force            |no        |         |**yes** / **no**|Force the creation without any confirmation |
|resizefs         |yes       |         |                |Resize underlying FS together with the lv   |
|size             |yes       |         |**present**     |Change/set the lv size in units of megabytes|
|stripesize       |no        |         |**y** / **n**   |Number of kbs for the granularity of stripes|


Example Playbook
----------------

```yaml
    - name: lvextend
      hosts: servers
      roles:
         - system/glusterfs_lv/lvextend
```

License
-------

GNU General Public License 3.0

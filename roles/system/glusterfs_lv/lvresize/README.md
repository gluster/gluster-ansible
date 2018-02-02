lvresize
=========

lvresize role allows to resize a LogicalVolume

Requirements
------------
lvresize allows you to resize a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                                |
| ----------      | -------- | ------- | -------        | -----------                                |
|extents          |no        |         |                |Change/set the lv size in units of extents  |
|force            |no        |         |**yes** / **no**|Force the creation without any confirmation |
|poolmetadatasize |no        |         |                |Change/set the thin pool metadata lv size   |
|resizefs         |yes       |         |                |Resize underlying FS together with the lv   |
|size             |yes       |         |**present**     |Change/set the lv size in units of megabytes|
|stripesize       |no        |         |**y** / **n**   |Number of kbs for the granularity of stripes|

Example Playbook
----------------

```yaml
    - name: lvresize
      hosts: servers
      roles:
         - system/glusterfs_lv/lvresize
```

License
-------

GNU General Public License 3.0

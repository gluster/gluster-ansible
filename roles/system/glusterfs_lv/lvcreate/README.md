lvcreate
=========

lvcreate role allows to create a LogicalVolume

Requirements
------------
lvcreate allows you to create a LogicalVolume

Role Variables
-------------

| Parameters      | Required | Default | Choices                                      | Description                                                     |
| ----------      | -------- | ------- | -------                                      | -----------                                                     |
|cachemode        |no        |         |**passthrough**/**writeback**/**writethrough**|Determines when the writes to a cache LV are considered complete |
|chunksize        |no        |         |                                              |size of chunk for cache pool and thin pool logical volumes       |
|extents          |no        |         |                                              |Change/set the lv size in units of extents                       |
|poolmetadatasize |no        |         |                                              |Change/set the thin pool metadata lv size                        |
|poolmetadataspare|no        |         |  **y** / **n**                               |Change/set the thin pool metadata lv size                        |
|resizefs         |yes       |         |                                              |Resize underlying FS together with the lv                        |
|size             |yes       |         |**present**                                   |Change/set the lv size in units of megabytes                     |
|stripesize       |no        |         |**y** / **n**                                 |Number of kbs for the granularity of stripes                     |
|thin             |no        |         |**present**                                   |Creates thin pool or thin logical volume or both                 |
|thinpool         |no        |         |                                              |Specifies the name of thin pool volume name                      |
|vitualsize       |yes       |         |**present**                                   |Creates a thinly provisioned device of the given size            |
|wipesignature    |no        |         |**y** / **n**                                 |Controls wiping of detected signatures on new Logical Volume     |
|zero             |no        |         |**y** / **n**                                 |Controls zeroing of the first 4KiB of data in the new LV         |

Example Playbook
----------------

```yaml
    - name: lvcreate
      hosts: servers
      roles:
         - system/glusterfs_lv/lvcreate
```

License
-------

GNU General Public License 3.0

mount
=========
To mount a gluster file system

Role Variables
--------------

| Parameters      | Required | Default | Choices | Description                      |
| ----------      | -------- | ------- | ------- | -----------                      |
|path             |yes       |         |         |                                  |
|src              |yes       |         |         | target(mountpoint)/source(device)|
|fstype           |yes       |         | **xfs** | File system type                 |
|opts             |no        |         |         | Extra options for mount          |

Example Playbook
----------------

```yaml
    - name: mount
      hosts: servers
      roles:
         - system/glusterfs_mount
```

License
-------

GNU General Public License 3.0

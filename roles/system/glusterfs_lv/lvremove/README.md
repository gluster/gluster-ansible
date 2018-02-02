lvremove
=========

lvremove role allows to remove a LogicalVolume

Requirements
------------
lvremove allows you to remove a LogicalVolume

Role Variables
--------------

| Parameters      | Required | Default | Choices        | Description                                |
| ----------      | -------- | ------- | -------        | -----------                                |
|force            | no       |         |**yes** / **no**|Force the creation without any confirmation |

Example Playbook
----------------

```yaml
    - name: lvremove
      hosts: servers
      roles:
         - system/glusterfs_lv/lvremove
```

License
-------

GNU General Public License 3.0

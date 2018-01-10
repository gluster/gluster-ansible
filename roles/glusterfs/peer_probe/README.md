Role Name
=========

peer_probe - Probe a list of peers into a cluster.

Requirements
------------
This role requires glusterfs_peer module to be present.

Role Variables
--------------

| Parameters  | Required | Default | Choices | Description |
| ----------  | -------- | ------- | ------- | ----------- |
|state        |yes       |         |**present**|Create a Trusted Storage Pool|
|nodes        |yes       |         |         |The nodes that are to be added to the Trusted Storage Pool.|


Example Playbook
----------------

```yaml
    - name: glusterfs_peer
      hosts: servers
      roles:
         - glusterfs/peer_probe
```


License
-------

GPLv3

Author Information
------------------

Devyani Kota <dkota@redhat.com>

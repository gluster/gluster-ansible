backend-reset
=============

Resets the backend of GlusterFS clusters.

Requirements
------------

Ansible 2.3 and above
GlusterFS 3.x and above

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

The roles imported here are:
- glusterfs_umount
- glusterfs_lvremove
- glusterfs_vgremove
- glusterfs_pvremove

Example Playbook
----------------

Create backend for GlusterFS clusters.

```yaml
    - name: backend-reset
      hosts: servers
      roles:
         - system/backend-reset

```

License
-------

GNU General Public License 3.0

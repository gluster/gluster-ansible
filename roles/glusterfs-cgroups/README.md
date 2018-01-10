glusterfs-cgroups
=========

Configures a systemd slice unit for glusterfs processes to limit the CPU Quota used by these processes. glusterd service is restarted once configured for changes to take effect


Role Variables
--------------

| Parameters   | Required | Default | Choices  | Description |
| ----------   | -------- | ------- | -------  | ----------- |
|cgroup_cpu_quota        |no       |400%         | a percentage value, suffixed with "%" to set the CPU time quota to processes. Use values > 100% for allotting CPU time on more than one CPU|


Example Playbook to call the role
---------------------------------

```yaml
    - hosts: servers
      remote_user: root
      roles:
         - glusterfs-cgroups
```


License
-------

GNU General Public License 3.0

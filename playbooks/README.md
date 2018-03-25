There is a playbook which has 3 separate plays

1. LVM

2. Filesystem

3. Glusterfs

Executing playbook:
```
ansible-playbook -u user -e storage_type="glusterfs" glusterfs-playbook.yml --tags=""
```


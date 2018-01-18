#!/bin/bash

# Copy the roles to /etc/ansible/roles
for f in ../roles/*; do
    if test -d $f; then
        sudo cp -r $f /etc/ansible/roles
    fi
done

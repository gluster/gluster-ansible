# Contributing

Thank you for contributing to Gluster Ansible. This document explains how the repository is organized and how to submit contributions.

**Table of Contents**

- [Introduction](#introduction)
- [Submitting contributions](#submitting-contributions)

## Introduction

This repository consists of Ansible roles that are used to install, deploy, and configure various parts of the GlusterFS project.

We have the following categories into one of which your Ansible role might fit into:

* cns-deploy
* ctdb
* geo-replication
* glusterfs
* nfs-ganesha
* quota
* system


If it does not fit any of the above categories feel free to create one.

## Submitting contributions

1. Fork the repo and make changes in your local repo.
2. Make changes and commit. You may want to review your changes and run tests
   a. Ensure that you write a README.md for your role explaining the variables supported in the role. An example role can be found [here](https://github.com/gluster/gluster-ansible/tree/master/roles/system/glusterfs_pv/pvchange).
   b. Test the role and provide at least one playbook which uses the role.
3. [Open a Pull Request](https://help.github.com/articles/creating-a-pull-request/). Give it a meaningful title explaining the changes you are proposing, and
   then add further details in the description.


# Running the tests locally

The tests bring up docker containers using a `provision_docker` role. 
`docker` needs to be running on the VM or server that you are running these tests.
Here's how

### Install pre-requisites
```
# yum install docker ansible
```

You need to ensure `provision_docker` is installed under your tests directory

```
# ansible-galaxy install -r tests/requirements.yml -p tests/roles/ 
```

### Running the test

```
# ansible-playbook -i tests/inventory tests/test_docker.yml
```


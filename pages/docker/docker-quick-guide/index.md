title: Docker quick guide
content:

List containers
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
41d307cda913        training/webapp     "python app.py"     12 minutes ago      Up 12 minutes       0.0.0.0:32768->5000/tcp   desperate_archimedes
```

Logs / stdout
```
$ docker logs desperate_archimedes
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.16.0.20 - - [30/May/2016 18:23:55] "GET / HTTP/1.1" 200 -
172.16.0.20 - - [30/May/2016 18:23:56] "GET /favicon.ico HTTP/1.1" 404 -
```

Run interactive command.
- ubuntu is the image you would like to run.
- -t flag assigns a pseudo-tty or terminal inside the new container.
- -i flag allows you to make an interactive connection by grabbing the standard in (stdin containter)
- /bin/bash launches a Bash shell inside our container.
```
$ docker run -t -i ubuntu /bin/bash
```

Container’s processes
```
$ docker top desperate_archimedes
PID                 USER                COMMAND
854                 root                python app.py
```

Stop container
```
$ docker stop desperate_archimedes
```

Start container
```
$ docker start desperate_archimedes
```

Removing container
```
$ docker stop desperate_archimedes

$ docker rm desperate_archimedes
```

Docker name
```
$ docker run -d -P --name web training/webapp python app.py
```

## Docker networking

List networks
```
$ docker network ls

NETWORK ID          NAME                DRIVER
18a2866682b8        none                null
c288470c46f6        host                host
7b369448dccb        bridge              bridge
```

Inspect network
```
$ docker network inspect bridge

[
    {
        "Name": "bridge",
        "Id": "f7ab26d71dbd6f557852c7156ae0574bbf62c42f539b50c8ebde0f728a253b6f",
        "Scope": "local",
        "Driver": "bridge",
        "IPAM": {
            "Driver": "default",
            "Config": [
                {
                    "Subnet": "172.17.0.1/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
...
```

Create your own bridge network
```
$ docker network create -d bridge my-bridge-network

$ docker network ls

NETWORK ID          NAME                DRIVER
7b369448dccb        bridge              bridge
615d565d498c        my-bridge-network   bridge
18a2866682b8        none                null
c288470c46f6        host                host

$ docker network inspect my-bridge-network
```

Add containers to a network
$ docker run -d --net=my-bridge-network --name db training/postgres

Inspect container network settings
$ docker inspect --format='{{json .NetworkSettings.Networks}}' db

# Volumes

Create volumen with the same layer `training/postgres`
$ docker create -v /dbdata --name dbstore training/postgres /bin/true

Create a container db1 with the volumen
$ docker run -d --volumes-from dbstore --name db1 training/postgres

Create a container db2 with the volumen
$ docker run -d --volumes-from dbstore --name db2 training/postgres

# Building an image from a Dockerfile
```
$ mkdir mycentos
$ cd mycentos
```

```
$ vi Dockerfile

# THIS IS A COMMENT
FROM centos
MAINTAINER Diego Najar
RUN yum update -y
```

```
$ docker build -t dignajar/mycentos:v2 .
```

# Push an image to Docker Hub
https://hub.docker.com/

```
$ docker push dignajar/mycentos
```

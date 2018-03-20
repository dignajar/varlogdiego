# Title: Creating your first Docker container
<!-- Position: 1 -->
---
Download Docker CentOS image from Docker Hub.
```
$ docker pull centos
```

Create a new container with the image and execute `/bin/bash` to access to the shell.
```
$ docker run -i -t centos /bin/bash
```

Make the changes inside the container and type `exit`.

Get the container ID to create an image from it.
```
$ docker ps -a | grep centos | head -1 | awk '{print $1}'
065729c608d8
```

Commit the changes on a new image, the value `0253a35bce7f` is the ID of the container, and the tag `centos-mod:1.0`.
```
$ docker commit -a "Diego" -m "Updates" 065729c608d8 centos-mod:1.0
```

Get the list of images.
```
$ docker images
```

Run the container with the new image and get access to the shell.
```
$ docker run -i -t centos-mod:1.0 /bin/bash
```

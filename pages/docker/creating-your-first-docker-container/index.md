title: Creating your first Docker container
content:

Download CentOS image.
```
$ docker pull centos
```

Create a new container with the image.
```
$ docker run -i -t centos /bin/bash
```

Make the changes inside the container and type exit.

Commit the changes on a new image, the value `0253a35bce7f` is the ID of the container.
```
$ docker commit -a "Diego" -m "Updates" 0253a35bce7f centosModified
```

Get the list of images.
```
$ docker images
```

Run the container with the new image.
```
$ docker run -i -t centosModified /bin/bash
```

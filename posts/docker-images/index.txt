title: Creating your first Docker container
contnet:

Download centos image
$ docker pull centos

Create a new container with the image
$ docker run -i -t centos /bin/bash

Make the changes inside the container and type exit

Commit the changes on a new image
$ docker commit -a "Diego" -m "Updates" 0253a35bce7f centosModified

Get the list of images
$ docker images

Run the container with the new image
$ docker run -i -t centosModified /bin/bash

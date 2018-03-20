# Title: Docker registry
<!-- Position: 3 -->
---
## API Rest v2
Show image list
```
$ curl -v -X GET https://{docker-registry-url}/v2/_catalog
```

Show image tags
```
$ curl -v -X GET https://{docker-registry-url}/v2/{image-name}/tags/list
```

## Login
```
$ docker login <registry-host>:<registry-port>
```

## Pull, Tag and Push
Get the image `nginx:latest` from Docker Hub then tag it with the new repository and push it to the new repository.
```
$ docker pull nginx:latest
$ docker tag nginx:latest <registry-host>:<registry-port>/nginx:1.2
$ docker push <registry-host>:<registry-port>/nginx:1.2
```

## Run Docker Registry
```
$ docker run -d -p 80:5000 -p 5000:5000 --restart always -v /var/lib/registry:/var/lib/registry --name registry2 registry:2.6.2
```

## Clean-up Docker Registry
To clean up the registry you can use this Docker Image
- https://hub.docker.com/r/lhanxetus/deckschrubber/

```
$ docker run --rm lhanxetus/deckschrubber \
	-registry <https://registry-host> \
	-month 6 \
	-repos <repository/image> \
	-latest 20
```

After execute the script you need to execute the garbage collector from the registry.
```
# Stop the registry
$ docker stop registry2

# Execute Garbage collector, to complete this step remove the dry-run parameter
$ docker run -v /var/lib/registry:/var/lib/registry --rm registry:2.6.2 bin/registry garbage-collect --dry-run /etc/docker/registry/config.yml
```
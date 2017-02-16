Title: Docker registry

Content:

## API Rest v2

Show image list
```
curl -v -X GET https://{docker-registry-url}/v2/_catalog
```

Show image tags
```
curl -v -X GET https://{docker-registry-url}/v2/{image-name}/tags/list

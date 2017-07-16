# Title: Docker registry
<!-- Position: 3 -->
---
## API Rest v2

Show image list
```
curl -v -X GET https://{docker-registry-url}/v2/_catalog
```

Show image tags
```
curl -v -X GET https://{docker-registry-url}/v2/{image-name}/tags/list

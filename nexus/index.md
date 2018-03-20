# Title: Nexus
<!-- Position: 4 -->
---

## Upload binary file to Nexus
```
curl --request PUT \
	--user {USER}:{PASSWORD} \
	https://nexus.com/nexus/repository/{REPO_NAME}/file.zip --data @./file.zip \
	-H Content-Type:application/java-archive \
	--verbose
```
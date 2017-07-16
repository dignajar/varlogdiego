# Title: SSH Port Forwarding
<!-- Position: 1 -->
<!-- Date: 2016-03-10 18:20:00 -->
---
Synopsis:
```
ssh -L {local-port}:{host}:{host-port} {user}@{ssh-server}
```

Example:
```
ssh -L 8080:varlogdiego.com:443 my-user@my-server-with-ssh
```

```
+------------<----port 22-->---------------<--port 443-->------------+
|SSH Client|------------------|SSH Server|----------------|   Host   |
+----------+                  +----------+                +----------+
localhost:8080              my-server-with-ssh          varlogdiego.com:443
```

Link: http://www.linuxhorizon.ro/ssh-tunnel.html

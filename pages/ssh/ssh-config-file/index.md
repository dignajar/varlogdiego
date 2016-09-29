Title: SSH config file - tips and tricks

Content:

## ~/.ssh/config

```
Host dev
    HostName dev.example.com
    User diego
    Port 22
Host github.com
    IdentityFile ~/.ssh/github.key
```
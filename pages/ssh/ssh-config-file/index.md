Title: SSH config file - tips and tricks

Content:

## ~/.ssh/config

```
# For all hosts
Host *
     ForwardAgent no
     ForwardX11 no
     ForwardX11Trusted yes
     User diego
     Port 22
     Protocol 2
     ServerAliveInterval 60
     ServerAliveCountMax 30

# For host dev
Host dev
    HostName dev.example.com
    User devusr
    Port 8022

# For github.com
Host github.com
    IdentityFile ~/.ssh/github.key
```

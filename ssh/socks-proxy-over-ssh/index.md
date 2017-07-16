# Title: Socks proxy over SSH
<!-- Position: 1 -->
<!-- Date: 2016-03-10 18:20:00 -->
---

```
$ ssh -D 8080 -f -C -q user@ssh-server
```

- `-D` socks tunnel over port 8080
- `-f` process to background
- `-C` compress the data before sending it
- `-q` quiet mode

Configure Firefox->Preferences->Network->Settings->Manula proxy configuration->SOCKS Host


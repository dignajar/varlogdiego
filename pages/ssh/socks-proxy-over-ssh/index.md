Title: Socks proxy over SSH

Content:

```
$ ssh -D 8080 -f -C -q user@ssh-server
```

- `-D` socks tunnel over port 8080
- `-f` process to background
- `-C` compress the data before sending it
- `-q` quiet mode

Configure Firefox->Preferences->Network->Settings->Manula proxy configuration->SOCKS Host


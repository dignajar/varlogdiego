Title: Nginx + PHP-FPM + Tuning

Content:

## Tuning PHP

### User and Group
```
[www]
...
user = nginx
group = nginx
...
```

### Unix sockets
Edit the file /etc/php-fpm.d/www.conf

```
[www]
....
listen = /var/run/php-fpm/php-fpm.sock
listen.owner = nginx
listen.group = nginx
listen.mode = 0660
```

### TCP Sockets
Listen directive to TCP, IP:Port.

Edit the file /etc/php-fpm.d/www.conf
```
listen = 127.0.0.1:9000
```

### Restart child processes when die*

If `emergency_restart_threshold` amount of child processes exit with segmentation fault, page fault, and access violation (SIGSEGV or SIGBUS) within the time interval set by `emergency_restart_interval` then FPM will restart

```
emergency_restart_threshold 10
emergency_restart_interval 1m
process_control_timeout 10s
```

### Sources
- http://myjeeva.com/php-fpm-configuration-101.html
- https://tweaked.io/guide/nginx/
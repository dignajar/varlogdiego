# Title: lsof
<!-- Date: 2017-10-01 22:00:00 -->
<!-- dateModified: 2017-11-01 22:00:00 -->
---

## Show procces which opened a specific file
```
$ lsof /var/log/php7.0-fpm.log

COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
php-fpm7. 961 root    2w   REG    8,1       56 137022 php7.0-fpm.log
php-fpm7. 961 root    4w   REG    8,1       56 137022 php7.0-fpm.log
```

## List opened files under a directory
```
$ lsof +D /var/log/

COMMAND     PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd    840 syslog    5w   REG    8,1    31274 130646 /var/log/syslog
rsyslogd    840 syslog    6w   REG    8,1    14389 137170 /var/log/auth.log
rsyslogd    840 syslog    7w   REG    8,1    13514 137148 /var/log/kern.log
nginx       955   root    2w   REG    8,1        0 456300 /var/log/nginx/error.log
nginx       955   root    4w   REG    8,1        0 456300 /var/log/nginx/error.log
...
```

## List files opened by a specific user
```
$ lsof -u <username>
```

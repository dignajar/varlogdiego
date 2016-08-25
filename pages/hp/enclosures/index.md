Title: HP Onboard Administrator command line
Content:

This commands are for the HP OA via SSH.

Set NTP, primary and secondary.
```
$ set ntp primary {NTP_IP_ADDRESS}
$ set ntp secondary {NTP_IP_ADDRESS}
$ enable ntp
```

Set Timezone.
```
$ set timezone US/Eastern
```

Set remote syslog.
```
$ set remote syslog server {SYSLOG_IP_ADDRESS}
$ set remote syslog port {SYSLOG_PORT}
$ enable syslog remote
```

Set OA name / hostname.
```
$ set oa name 1 {NEW_NAME_FOR_OA_PRIMARY}
$ set oa name 2 {NEW_NAME_FOR_OA_SECONDARY}
```

Set alert email address.
```
$ set alertmail mailbox {EMAIL_TO}
$ set alertmail smtpserver {SMTP_IP_ADDRESS}
$ set alertmail sendername {SENDER_NAME}
$ set alertmail senderemail {EMAIL_FROM}
$ enable alertmail
```

Connect to some ILO blade.
```
$ connect server {BAY_NUMBER}
```

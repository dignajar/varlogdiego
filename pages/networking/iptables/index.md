Title: Iptables basic commands

Content:

## NAT tables

List NAT table

```
$ iptables -t nat -L
```

Delete NAT rule

```
# Show rules with number line
$ iptables -t nat --line-numbers -L

# Delete rule by the number line
$ iptables -t nat -D PREROUTING {LINE NUMBER}
```

Add forwarding port on localhost

```
# Syntax
$ iptables -t nat -A PREROUTING -i {INTERFACE} -p tcp --dport {FROM PORT} -j REDIRECT --to-port {TO PORT}

# Enable forwarding support on Linux
$ sysctl net.ipv4.ip_forward=1

# Example, forwarding all TCP connection to port 4443 to 443
$ iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 4443 -j REDIRECT --to-port 443
```


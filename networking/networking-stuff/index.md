# Title: Networking stuff
<!-- Position: 1 -->
<!-- Description: Networking commands for GNU/Linux -->
<!-- Tags: Networking, Commands -->
<!-- Date: 2016-03-10 18:20:00 -->
---
## Enable or disable network interface

```
# Enable
$ ip link set eth1 up
```

```
# Disable
$ ip link set eth1 down
```

## Add static routes and default Gateway

```
# Static route
# ip route add {NETWORK/MASK} via {GATEWAY-IP} dev {DEVICE}
$ ip route add 10.1.1.0/24 via 10.1.1.1 dev eth0
```

```
# Default gw
# ip route add default via {GATEWAY-IP}
$ ip route add default via 10.1.1.1
```

# Title: tcpdump basic commands
<!-- Position: 1 -->
<!-- Tags: Networking, tcpdump -->
<!-- Date: 2016-03-10 18:20:00 -->
---
## Exclude network
```
# Syntax
$ tcpdump -n -i {INTERFACE} not dst net {SUBNET}

# Example, capture package from interface eth0 and exclude the subnet 10.0.0.0/16
$ tcpdump -n -i eth0 not dst net 10.0.0.0/16
```


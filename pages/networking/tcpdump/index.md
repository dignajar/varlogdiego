Title: tcpdump basic commands

Content:

## Exclude network

```
# Syntax
$ tcpdump -n -i {INTERFACE} not dst net {SUBNET}

# Example, capture package from interface eth0 and exclude the subnet 10.0.0.0/16
$ tcpdump -n -i eth0 not dst net 10.0.0.0/16
```


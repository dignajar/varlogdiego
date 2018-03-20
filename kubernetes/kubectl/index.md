# Title: Kubectl
<!-- Date: 2017-10-01 22:00:00 -->
<!-- dateModified: 2017-11-01 22:00:00 -->
---

## Run a Pod
Run a pod with the Alpine image, keep it in the foreground and do not restart if it exit.
```
$ kubectl run -i -t alpine --image=alpine --restart=Neverl
```

## Nodes CPU Requests and Memory Requests
```
$ kubectl describe nodes | grep -A 2 -e "^\\s*CPU Requests"

CPU Requests	CPU Limits	Memory Requests	Memory Limits
------------	----------	---------------	-------------
3710m (92%)	10100m (252%)	7408Mi (46%)	13120Mi (82%)
```

## Nodes CPU Used and Memory Used
```
$ kubectl top nodes

NAME                                        CPU(cores)   CPU%      MEMORY(bytes)   MEMORY%
ip-10-1-1-10.eu-central-1.compute.internal   290m         7%        11018Mi         69%
ip-10-1-1-11.eu-central-1.compute.internal   362m         9%        11285Mi         70%
```
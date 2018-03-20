# Title: Kubernetes
<!-- Date: 2017-01-01 22:00:00 -->
<!-- dateModified: 2017-01-01 22:00:00 -->
---
## Installation on CentOS 7

### Prepare all hosts

Disable firewall
```
$ systemctl stop firewalld
$ systemctl disable firewalld
```

Install NTP daemon and enable it
```
$ yum -y install ntp
$ systemctl start ntpd
$ systemctl enable ntpd
```

Add the entry of your hosts in `/etc/hosts`
```
...
10.0.0.50 kuber-master
10.0.0.51 kuber-slave01
10.0.0.52 kuber-slave02
...
```

Add the repository for the manage package
```
vi /etc/yum.repos.d/virt7-docker-common-release.repo

# Add this lines inside

[virt7-docker-common-release]
name=virt7-docker-common-release
baseurl=http://cbs.centos.org/repos/virt7-docker-common-release/x86_64/os/
gpgcheck=0
```

Install the components of Kubernetes
```
$ yum -y install --enablerepo=virt7-docker-common-release kubernetes etcd flannel
```

Common Kubernetes configuration, edit the file `/etc/kubernetes/config`
```
KUBE_ETCD_SERVERS="--etcd-servers=http://kuber-master:2379"
KUBE_LOGTOSTDERR="--logtostderr=true"
KUBE_LOG_LEVEL="--v=0"
KUBE_ALLOW_PRIV="--allow-privileged=false"
KUBE_MASTER="--master=http://kuber-master:8080"
```

Configure the Flannel service, edit the file `/etc/sysconfig/flanneld`
```
FLANNEL_ETCD="http://kuber-master:2379"
FLANNEL_ETCD_KEY="/kuber-centos/network"
FLANNEL_OPTIONS=""
```

### Master

Configure etcd, edit the file `/etc/etcd/etcd.conf`
```
# [member]
ETCD_NAME=default
ETCD_DATA_DIR="/var/lib/etcd/default.etcd"
ETCD_LISTEN_CLIENT_URLS="http://0.0.0.0:2379"

#[cluster]
ETCD_ADVERTISE_CLIENT_URLS="http://0.0.0.0:2379"
```

Configure the API server, edit the file `/etc/kubernetes/apiserver`
```
KUBE_API_ADDRESS="--address=0.0.0.0"
KUBE_API_PORT="--port=8080"
KUBELET_PORT="--kubelet-port=10250"
KUBE_ETCD_SERVERS="--etcd-servers=http://kuber-master:2379"
KUBE_SERVICE_ADDRESSES="--service-cluster-ip-range=10.100.0.0/16"
KUBE_ADMISSION_CONTROL=""
KUBE_API_ARGS=""
```

Enable, and restart the daemons / services
```
for service in etcd kube-apiserver kube-controller-manager kube-scheduler flanneld; do
    systemctl enable $service
    systemctl restart $service
    systemctl status $service
done
```

Configure the Flannel network
```
$ etcdctl mkdir /kuber-centos/network
$ etcdctl mk /kuber-centos/network/config "{ \"Network\": \"10.100.0.0/16\", \"SubnetLen\": 24, \"Backend\": { \"Type\": \"vxlan\" } }"
```

### Minions nodes

Configure Kubelet service, edit the file `/etc/kubernetes/kubelet`
```
KUBELET_ADDRESS="--address=0.0.0.0"
KUBELET_PORT="--port=10250"
KUBELET_HOSTNAME="--hostname-override=kuber-slave01"
KUBELET_API_SERVER="--api-servers=http://kuber-master:8080"
KUBELET_ARGS=""
```

Configure both minions node, and change the `KUBELET_HOSTNAME` on each one.

Enable, and restart the daemons / services
```
for service in kube-proxy kubelet docker flanneld; do
    systemctl enable $service
    systemctl restart $service
    systemctl status $service
done
```

## Check the system

Check routes on master
```
$ route -n

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.0.1     0.0.0.0         UG    0      0        0 eth0
10.100.0.0      0.0.0.0         255.255.0.0     U     0      0        0 flannel.1
192.168.0.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

Check routes on minions nodes
```
$ route -n

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.0.1     0.0.0.0         UG    0      0        0 eth0
10.100.0.0      0.0.0.0         255.255.0.0     U     0      0        0 flannel.1
10.100.12.0     0.0.0.0         255.255.255.0   U     0      0        0 docker0
192.168.0.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

Check nodes on master and minions
```
$ kubectl get nodes

NAME            STATUS    AGE
kuber-slave01   Ready     2d
kuber-slave02   Ready     2d
```

## Deploy an Nginx cluster

Create a cluster of two nginx containers. The images is downloaded from Docker Hub.
```
$ kubectl run my-nginx --image=nginx --replicas=2 --port=80
```

Get the deployments
```
$ kubectl get deployments

NAME       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
my-nginx   2         2         2            2           5m
```

Get the pods, filtered by the deployment name `my-nginx`
```
$ kubectl get pods -l run=my-nginx -o wide

NAME                        READY     STATUS    RESTARTS   AGE
my-nginx-3800858182-4xjui   1/1       Running   0          28m       kuber-slave01
my-nginx-3800858182-djz5t   1/1       Running   0          28m       kuber-slave02
```

Get the pods IP and where are running, filtered by the deployment name `my-nginx`
```
$ kubectl get pods -l run=my-nginx -o yaml | grep "nodeName\|podIP"

# my-nginx-3800858182-4xjui
nodeName: kuber-slave01
podIP: 10.100.12.2

# my-nginx-3800858182-djz5t
nodeName: kuber-slave02
podIP: 10.100.30.2
```

Make some test with curl from differents nodes.
```
$ curl -vvv 10.100.12.2

$ curl -vvv 10.100.30.2
```

### Deploy a load balancer for the Nginx cluster

Deploy the load balancer for the deployment `my-nginx`
```
$ kubectl expose deployment my-nginx --port=80 --type=LoadBalancer
```

Get the list of services
```
$ kubectl get services

NAME         CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
my-nginx     10.100.246.92                 80/TCP    28s
```

Test the load balancer
```
$ curl -vvv 10.100.246.92
```
Title: How to install BOSH on Amazon AWS

Date: 2016-10-26 12:00:00

DateModified: 2016-12-05 22:00:00

Content:

## 1- AWS Environment

Prepare the AWS environment, VPC, Subnet, security groups, etc.

### VPC
```
# Create a VPC: echo-vpc
10.100.0.0/16
```

### VPC: Subnet
```
# Create a subnet: echo-subnet-public
10.100.10.0/24
```

### VPC: Route table
```
# Create a route table: echo-rt-public

10.100.0.0/16   ->  local
0.0.0.0/0       ->  Internet Gateway
```

### VPC: Security Group
```
# Create a security group: echo-sg-public

All traffic         from        10.100.0.0/16
SSH                 from        {JUMPBOX IP ADDRESS}
TCP Port 6868       from        {JUMPBOX IP ADDRESS}
TCP Port 25555      from        {JUMPBOX IP ADDRESS}
```

### VPC: Elastic IP
```
# Create an elastic IP for BOSH
```

### EC2: Key pairs
```
# Create a private key: echo.pem
```

### EC2: Instances
```
# It's highly recommended create a virtual machine for use as Jumpbox, then install all tools on this vm.
# Create a new instance on the subnet where will be BOSH (echo-subnet-public).
# You can use the private key echo.pem for your Jumpbox.
# t2.micro is enough but add extra disk on root partition.
```

## 2- Install bosh-init

BOSH init (bosh-init) is used for creating and updating a Director VM (and its persistent disk) in an environment.
- https://bosh.io/docs/install-bosh-init.html

### Debian/Ubuntu dependencies
```
$ sudo apt-get install -y build-essential zlibc zlib1g-dev ruby ruby-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3
```

### Redhat/Centos dependencies
```
$ sudo yum install gcc gcc-c++ ruby ruby-devel mysql-devel postgresql-devel postgresql-libs sqlite-devel libxslt-devel libxml2-devel yajl-ruby patch
```

### Download and install bosh-init
```
$ wget https://s3.amazonaws.com/bosh-init-artifacts/bosh-init-0.0.99-linux-amd64
$ sudo mv bosh-init-0.0.99-linux-amd64 /usr/local/bin/bosh-init
$ sudo chmod 755 /usr/local/bin/bosh-init
$ bosh-init -v

version 0.0.99-1c660f1-2016-11-11T23:51:52Z
```

## 3- Install BOSH Cli

BOSH Command Line Interface (CLI) is used to interact with the Director. The CLI is written in Ruby and is distributed via bosh_cli gem.
- https://bosh.io/docs/bosh-cli.html

### Debian/Ubuntu dependencies
```
$ sudo apt-get install -y build-essential ruby ruby-dev libxml2-dev libsqlite3-dev libxslt1-dev libpq-dev libmysqlclient-dev zlib1g-dev
```

### Redhat/Centos dependencies
```
$ sudo yum install gcc ruby ruby-devel mysql-devel postgresql-devel postgresql-libs sqlite-devel libxslt-devel libxml2-devel yajl-ruby
```

### Install BOSH Cli
```
$ gem install bosh_cli --no-ri --no-rdoc
$ bosh -v

BOSH 1.3262.24.0
```

## 4- Create the manifest bosh-aws.yml

You can use the manifest from here, or download a new and clean from here: https://bosh.io/docs/init-aws.html

- The private key (echo.pem) need to be in the same path as the manifest.
- Replace the fields with your values
- The follow manifest assign to BOSH the private IP __10.100.10.6__ and the public IP __{ELASTIC-IP}__

### Manifest bosh-aws.yml
```
---
name: bosh

releases:
- name: bosh
  url: https://bosh.io/d/github.com/cloudfoundry/bosh?v=260
  sha1: f8f086974d9769263078fb6cb7927655744dacbc
- name: bosh-aws-cpi
  url: https://bosh.io/d/github.com/cloudfoundry-incubator/bosh-aws-cpi-release?v=62
  sha1: f36967927ceae09e5663a41fdda199edfe649dc6

resource_pools:
- name: vms
  network: private
  stemcell:
    url: https://bosh.io/d/stemcells/bosh-aws-xen-hvm-ubuntu-trusty-go_agent?v=3312.7
    sha1: e11da993d8bad4305e4bc51117f1de88a63f76bb
  cloud_properties:
    instance_type: m3.xlarge
    ephemeral_disk: {size: 25_000, type: gp2}
    availability_zone: AVAILABILITY-ZONE # <--- Replace with Availability Zone

disk_pools:
- name: disks
  disk_size: 20_000
  cloud_properties: {type: gp2}

networks:
- name: private
  type: manual
  subnets:
  - range: 10.100.10.0/24
    gateway: 10.100.10.1
    dns: [10.100.10.2]
    cloud_properties: {subnet: SUBNET-ID} # <--- Replace with Subnet ID
- name: public
  type: vip

jobs:
- name: bosh
  instances: 1

  templates:
  - {name: nats, release: bosh}
  - {name: postgres, release: bosh}
  - {name: blobstore, release: bosh}
  - {name: director, release: bosh}
  - {name: health_monitor, release: bosh}
  - {name: registry, release: bosh}
  - {name: aws_cpi, release: bosh-aws-cpi}

  resource_pool: vms
  persistent_disk_pool: disks

  networks:
  - name: private
    static_ips: [10.100.10.6]
    default: [dns, gateway]
  - name: public
    static_ips: [ELASTIC-IP] # <--- Replace with Elastic IP

  properties:
    nats:
      address: 127.0.0.1
      user: nats
      # password: nats-password # <--- Uncomment & change

    postgres: &db
      listen_address: 127.0.0.1
      host: 127.0.0.1
      user: postgres
      # password: postgres-password # <--- Uncomment & change
      database: bosh
      adapter: postgres

    registry:
      address: 10.100.10.6
      host: 10.100.10.6
      db: *db
      http:
        user: admin
        # password: admin # <--- Uncomment & change
        port: 25777
      username: admin
      # password: admin # <--- Uncomment & change
      port: 25777

    blobstore:
      address: 10.100.10.6
      port: 25250
      provider: dav
      director:
        user: director
        # password: director-password # <--- Uncomment & change
      agent:
        user: agent
        # password: agent-password # <--- Uncomment & change

    director:
      address: 127.0.0.1
      name: my-bosh
      db: *db
      cpi_job: aws_cpi
      max_threads: 10
      user_management:
        provider: local
        local:
          users:
          # - {name: admin, password: admin} # <--- Uncomment & change
          # - {name: hm, password: hm-password} # <--- Uncomment & change

    hm:
      director_account:
        user: hm
        # password: hm-password # <--- Uncomment & change
      resurrector_enabled: true

    aws: &aws
      access_key_id: ACCESS-KEY-ID # <--- Replace with AWS Access Key ID
      secret_access_key: SECRET-ACCESS-KEY # <--- Replace with AWS Secret Key
      default_key_name: echo
      default_security_groups: [echo-sg-public]
      region: REGION  # <--- Replace with Region

    # agent: {mbus: "nats://nats:nats-password@10.100.10.6:4222"} # <--- Uncomment & change

    ntp: &ntp [0.pool.ntp.org, 1.pool.ntp.org]

cloud_provider:
  template: {name: aws_cpi, release: bosh-aws-cpi}

  ssh_tunnel:
    host: ELASTIC-IP # <--- Replace with your Elastic IP address
    port: 22
    user: vcap
    private_key: ./echo.pem # Path relative to this manifest file

  # mbus: "https://mbus:mbus-password@ELASTIC-IP:6868" # <--- Uncomment & change

  properties:
    aws: *aws
    # agent: {mbus: "https://mbus:mbus-password@0.0.0.0:6868"} # <--- Uncomment & change
    blobstore: {provider: local, path: /var/vcap/micro_bosh/data/cache}
    ntp: *ntp
```

### Enable debug mode for bosh-init
```
$ export BOSH_INIT_LOG_LEVEL=DEBUG
$ export BOSH_INIT_LOG_PATH=/tmp/bosh-init.log
```

### Deploy BOSH
```
$ bosh-init deploy bosh-aws.yml
```

### Connect to BOSH director
```
$ bosh target {ELASTIC_IP}
```
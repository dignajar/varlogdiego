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
10.100.0.0/16 -> local
0.0.0.0/0 -> Internet Gateway
```

### VPC: Security Group
```
# Create a security group: echo-sg-public
ALL TCP, ALL UDP from 10.100.0.0/16
SSH from {YOUR IP ADDRESS}
HTTP from 0.0.0.0/0
HTTPS from 0.0.0.0/0
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
# t2.micro is enough.
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

You can get a manifest from here: https://bosh.io/docs/init-aws.html

Remember, the private key (echo.pem) need to be in the same path as the manifest.

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
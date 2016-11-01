Title: How to install BOSH on Amazon AWS

Date: 2016-10-26 12:00:00

Content:

## 1- Install bosh-init

bosh-init is used for creating and updating a Director VM (and its persistent disk) in an environment. https://bosh.io/docs/install-bosh-init.html

Debian/Ubuntu dependencies
```
$ sudo apt-get install -y build-essential zlibc zlib1g-dev ruby ruby-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3
```

Redhat/Centos dependencies
```
$ sudo yum install gcc gcc-c++ ruby ruby-devel mysql-devel postgresql-devel postgresql-libs sqlite-devel libxslt-devel libxml2-devel yajl-ruby patch
```

Download and install bosh-init
```
$ wget https://s3.amazonaws.com/bosh-init-artifacts/bosh-init-0.0.98-linux-amd64
$ sudo mv bosh-init-0.0.98-linux-amd64 /usr/local/bin/bosh-init
$ sudo chmod 755 /usr/local/bin/bosh-init
$ bosh-init -v

version 0.0.98-1c660f1-2016-10-12T18:37:57Z
```

## 2- Install BOSH Cli

BOSH Command Line Interface (CLI) is used to interact with the Director. The CLI is written in Ruby and is distributed via bosh_cli gem. https://bosh.io/docs/bosh-cli.html

Debian/Ubuntu dependencies
```
$ sudo apt-get install build-essential ruby ruby-dev libxml2-dev libsqlite3-dev libxslt1-dev libpq-dev libmysqlclient-dev zlib1g-dev
```

Redhat/Centos dependencies
```
$ sudo yum install gcc ruby ruby-devel mysql-devel postgresql-devel postgresql-libs sqlite-devel libxslt-devel libxml2-devel yajl-ruby
```

Install BOSH Cli
```
$ gem install bosh_cli --no-ri --no-rdoc
```

## 3- AWS Environment

Prepare the AWS environment, VPC, Subnet, security groups, etc.

VPC
```
172.16.0.0/16
```

Subnet
```
najar-subnet-bosh: 172.16.0.0/24
```

Route table
```
najar-route-bosh: Internet Gateway
```

Security Group
```
najar-sg-bosh: ALL TCP, ALL UDP from 172.16.0.0/16
```

## 4- Create the manifest bosh-aws.yml

You can get a manifest from here: https://bosh.io/docs/init-aws.html

Enable debug mode for bosh-init
```
$ export BOSH_INIT_LOG_LEVEL=DEBUG
$ export BOSH_INIT_LOG_PATH=/tmp/bosh-init.log
```

Deploy
```
$ bosh-init deploy bosh-aws.yml
```

Connect to BOSH director
```
$ bosh target {ELASTIC_IP}
```
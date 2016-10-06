Title: How to make a release for BOSH

Content:

## Create the release directory

```
$ bosh init release {RELEASE NAME}
```

```
$ cd {RELEASE NAME}
$ tree .
.
|-- blobs
|-- config
|   `-- blobs.yml
|-- jobs
|-- packages
`-- src

5 directories, 1 file
```

When deploying your release, BOSH places compiled code and other resources in the `/var/vcap/` directory tree, which BOSH creates on the job VMs. The four directories you just created, jobs, packages, src, and blobs, appear on job VMs as `/var/vcap/jobs`, `/var/vcap/packages`, `/var/vcap/src`, and `/var/vcap/blobs`, respectively.
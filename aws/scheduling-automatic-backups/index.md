# Title: Scheduling Automatic Backups of Snapshot
<!-- Position: 1 -->
---
This script uses [boto3](https://github.com/boto/boto3) libraries. The script will create a snapshot of the volume with the ID `volumeID`, on the description of the snapshot will appear the expiration date.

Script: https://github.com/dignajar/amazon-aws-scripts/blob/master/snapshot.py

Change this lines on the script file with your properties.

```
# Volume ID for snapshot
volumenID = "vol-eb194f49"

# Username with permissions, credentials are in .aws/credentials
username = "snapshot"

# Region name
region = "us-east-1"

# Amount of snapshotl
snapshotAmount = 2
```

For example, if you create a snapshot on 25 May 2016, the snapshot will expire on 27 May 2016, the variable snapshotAmount has a number of expiration days.

To automate this function you can use `crontab`, and execute this script every day.
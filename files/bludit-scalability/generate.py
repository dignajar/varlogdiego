#!/usr/bin/python

import os
import subprocess
import json
import datetime

amountOfPosts=10001

content = """Content:
## Definition

Scalability is the capability of a system, network, or process to handle a growing amount of work, or its potential to be enlarged in order to accommodate that growth.[1] For example, it can refer to the capability of a system to increase its total output under an increased load when resources (typically hardware) are added. An analogous meaning is implied when the word is used in an economic context, where scalability of a company implies that the underlying business model offers the potential for economic growth within the company.

## Database scalability

A number of different approaches enable databases to grow to very large size while supporting an ever-increasing rate of transactions per second. Not to be discounted, of course, is the rapid pace of hardware advances in both the speed and capacity of mass storage devices, as well as similar advances in CPU and networking speed.

One technique supported by most of the major database management system (DBMS) products is the partitioning of large tables, based on ranges of values in a key field. In this manner, the database can be scaled out across a cluster of separate database servers. Also, with the advent of 64-bit microprocessors, multi-core CPUs, and large SMP multiprocessors, DBMS vendors have been at the forefront of supporting multi-threaded implementations that substantially scale up transaction processing capacity.

From [Wikipedia](https://en.wikipedia.org/wiki/Scalability)
"""

dirName = "scalability-post-number-"

currentDate = datetime.datetime.now() - datetime.timedelta(days=amountOfPosts)

for i in range(1, amountOfPosts):
	if not os.path.exists("bl-content/posts/"+dirName+str(i)):
		os.makedirs("bl-content/posts/"+dirName+str(i))
	fHandle = open("bl-content/posts/"+dirName+str(i)+"/index.txt","w")
	fHandle.write("Title: Scalability post number "+str(i)+"\n Date: "+currentDate.strftime("%Y-%m-%d %H:%M:00")+"\n"+content)
	fHandle.close()
	currentDate += datetime.timedelta(days=1)
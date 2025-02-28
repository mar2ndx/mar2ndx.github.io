---
title: "[Design] MapReduce Intro"
category: Design
tags: []
comments: true
date: 2014-08-05 00:00
---


### An Overview

**[MapReduce](http://searchcloudcomputing.techtarget.com/definition/MapReduce) is a software framework**, or a **[distributed programming model](http://www.theserverside.com/news/1321219/Why-Should-You-Care-About-MapReduce)** intended for processing massive amounts of data in large clusters.

1. **Map**, a function that parcels out work to different nodes in the distributed cluster.

1. **Reduce**, another function that collates the work and resolves the results into a single value.

### More Info

**MapReduce isn't intended to replace relational databases**: it's intended to provide a lightweight way of programming things so that they can run fast by running in parallel on a lot of machines. Google uses MapReduce for **indexing every Web page** they crawl.

MapReduce framework is **fault-tolerant** because each node in the cluster is expected to report back periodically with completed work and status updates. If a node remains silent for longer than the expected interval, a master node makes note and re-assigns the work to other nodes.

**From a Senior Software Engineer at Google**:

> The key to how MapReduce works is to take input as, conceptually, a list of records. The records are split among the different computers in the cluster by Map. The result of the Map computation is a list of key/value pairs. Reduce then takes each set of values that has the same key and combines them into a single value. So Map takes a set of data chunks and produces key/value pairs and Reduce merges things, so that instead of a set of key/value pair sets, you get one result. You can't tell whether the job was split into 100 pieces or 2 pieces...

### Why MapReduce

MapReduce is important because it allows ordinary developers to use MapReduce library routines to create parallel programs without having to worry about programming for intra-cluster communication, task monitoring or failure handling.

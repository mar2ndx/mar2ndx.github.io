---
title: "[Design] Big Data Storage "
category: Design
tags: []
comments: true
date: 2015-01-06 00:00
---


[ref](http://www.mitbbs.com/article/JobHunting/32580869_0.html)

### Question

**Given 1 trillion messages** on fb and each message has at max 10 words.

How do you build the **index table** and how many machines do you need on the **cluster** to store the index table?

### One possible answer

Total data = 1 trillion _ 10 words _ 6 bytes / word = 60TB = one small NetApp box

**Index by hashed userid**; will distribute traffic effectively across servers; cache active users recent messages in memory.

[Cannot use Netapp box](http://www.glassdoor.com/Interview/Given-a-set-of-n-jobs-with-start-time-end-time-cost-find-a-subset-so-that-no-2-jobs-overlap-and-the-cost-is-maximum-QTN_440168.htm). From what I read in FB engg blog, they have all the info in main memory of server.

Total data = 1 trillion _ 10 words _ 6 bytes / word = 60TB + 1TB for Indexes.

Considering servers have 64 GB ram. 61 GB usable to store index, 1000 servers.

#### For more information

Read 2 other posts: **[Design] Distributed hash table** and **[Design] Cloud, Grid and Cluster**.

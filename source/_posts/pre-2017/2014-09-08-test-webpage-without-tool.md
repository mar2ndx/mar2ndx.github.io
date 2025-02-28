---
title: "[CC150v4] 11.4 Test Webpage without Tools "
category: CC150v4
tags: []
comments: true
date: 2014-09-08 00:00
---


### Question

> How would you load test a webpage without using any test tools?

### Solution

#### Load testing

**[Load testing](http://en.wikipedia.org/wiki/Load_testing)** is testing under normal and peak load condition. It's also called software performance testing, reliability testing, and volume testing.

#### Steps

**First identify the performance-critical scenarios**, which might include:

1. response time
1. throughput
1. resource utilization
1. max load that system can bear

**Then, design tests to simulate the load**: we can create virtual users by a multi-threaded program with 1000 thread, each acting as a user loading the page. We measure response time of each user.

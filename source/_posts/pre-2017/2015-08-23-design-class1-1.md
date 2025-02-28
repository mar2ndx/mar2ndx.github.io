---
title: "[NineChap System Design] Class 1.1: Overview "
category: NineChap
tags: []
comments: true
date: 2015-08-23 00:00
---


# Overview

## defination

the process of defining the **architecture, components, modules, interfaces and data** to satisfy specified **requirements**.

1. conceptual design (macro)
2. logical design
3. physical design (micro)

### Top-down design

Eg. MS Office, Huawei Security System

### Bottom-up design

Most start-up use, MVP first using Medetor + MongoDb.

## 5 steps (SNAKE Principle):

1. **Scenario**: case/interface - input
1. **Necessary**: constrain/hypothesis - input
1. **Application**: service/algorithm - output
1. **Kilobit**: data - output
1. **Evolve** - solution

# A top-down example

Example one: **design a radio**

## Step One, Scenario

1. brain storm

   1. register/log in
   1. play music
   1. recommendation

1. prioritize

   1. play music
      1. Get channel
      1. select a channel
      1. play

## Step Two, Necessary

1. ask

   1. total user - 100,000,000
   1. **daily users - 1,000,000**

1. predict

   1. user analysis
   1. Traffic analysis
   1. Memory analysis
   1. QPS

Details:

1. user analysis

   > Avg Concurrent users = daily users **/ 5** = 200,000
   >
   > Peak Concurrent users = concurrent user **\* 3** = 600,000

   considering your product may grow in the next 3 month:

   > Max Peak users in 3 month = Peak users **\* 10** = 6,000,000

1. Traffic analysis

   > Request of new music per user: 1 music/min
   >
   > Music size = 3MB
   >
   > Max peak traffic (in 3 months) = 6,000,000 \* 3MB / 60 = 300GB/s

1. Memory analysis

   > Memory per user (metadata) = 10KB
   >
   > Max daily memory = 1,000,000 \* 10 \* 10 = 100 million KB = 100GB
   >
   > (10 times of avg daily user)

## Step Three, Application

1. Replay the case, one service for each
1. Merge the services

![](/images/design-class1-basic-receptionist.png)

## Step Four, Kilobit: data

1. Append 1 dataset for each service

   Eg. User service: stability, more addition, less modify and deletion.

   Eg. Channel Service: high concurrency, MongoDB

   Eg. Music Service: MP3 File Systems

![](/images/design-class1-reco-5.png)

## Last Step, Evolve

1. Better: constrains

   eg. able to handle 300GB/s traffic?

1. Broader: new cases

   share music? delete user account?

1. Deeper: details design

From views of **Performance, Scalability and Robustness**.

![](/images/design-class1-snake.jpg)

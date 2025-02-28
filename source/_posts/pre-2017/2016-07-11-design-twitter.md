---
title: "[Design] Design Twitter"
category: Design
tags: []
comments: true
date: 2016-07-11 00:00
---


# System design evaluation form

1. work solution
1. special cases
1. analysis
1. trade off
1. knowledge base

# Design guideline: 4S

1. Scenario

   ask, features, qps, DAU, interfaces

1. Service

   split, application, module

1. Storage

   schema, data, sql, NoSql, file system

1. Scale

   sharding, optimize, special case

# Scenario

## DAU?

Whta's the DAU/MAU rate?

Chatting apps like wechat/whatapp has a rate of around 75%, but facebook/twitter is lower at 60%.

## Enumerate the functions

1. registration
1. user profile display/edit
1. upload image/video
1. search
1. post a tweet
1. share a tweet
1. timeline
1. newsfeed
1. follow/unfollow

## QPS

1. concurrent user

   150M user * 60 query/user / 60*60\*24s = average QPS = 100K

   **peak QPS = 3 \* average QPS = 300K**

   fast growing product = 2 \* peak QPS = 600K

1. read qps: 300K QPS
1. write qps: 5K QPS

On average, **a web server support around 1000 QPS**, thus in this case, we need 300 servers to support the system.

# Service

## 4 services for Twitter

![](/images/jiuzhang-four-service.png)

1. user service
   1. register
   2. login
1. tweet service
   1. post tweet
   1. news feed
   1. timeline
1. media service
   1. upload image
   1. upload video
1. friendship service
   1. follow
   1. upfollow

# Storage

1. SQL

   **Good for** accurate, small amount of data, more read than write.
   user table

2. NoSQL

   **Good for** large amount of read/write, high scalability.
   tweets
   social graph (follower)

3. File System

   **Good for** media files
   photo, video

## Select the right DB

![](/images/jiuzhang-db-selection.png)

**Question: can we use file system for tweets**?

No, it's hard to query. Eg. query all tweets of my friends.

## Design data schema

(optional) 3 tables needed:

1. user table
2. tweet table
3. friendship table: this is not as straight forward, as it shall contain double directions info

![](/images/jiuzhang-data-schema.png)

# Important: News Feed

## pull model

Read top 50 feeds from top 100 friends, then merge sort by date. (note that user is getting sync-blocked here).

Post tweet is simple 1 DB write.

**This design is bad, because file-system/DB read is slow**. If you have N friends, you query O(N) DB queries. **It's too slow (and user is getting sync-blocked, too)**. We should have, ideally, <= 7 DB queries per web page.

![](/images/jiuzhang-pull-diagram.png)

![](/images/jiuzhang-pull-code.png)

### problem

1. synchronously block user from getting news feed
1. too many DB reads

## push model

Each person have a list storing new feeds. When friend post tweet, **fanout** to my feed list.

When I read, I simply read top 100 from the feed list. **So read is 1 DB read**.

Post tweet is N DB writes, which is slow. **However this is done async, so it does not matter**.

![](/images/jiuzhang-push-diagram.png)

![](/images/jiuzhang-push-code.png)

One example of async implementation: **RabbitMQ**

# Scale

## optimize pull model

Although it looks like push is faster than pull, **facebook and twitter both use pull model**.

1. add cache for DB, reduce # of DB read
2. also cache each user's news feed

   your yesterday's feeds are all cached, thus don't need to read everytime.

## optimize push model

1. disk waste a lot, although disk is cheap
1. inactive user!

   rank follower by weight, and don't write to inactive user (eg. last login time)

1. if follower is toooo much, like Lady Gaga, user pull for Lady Gaga.

   Tradeoff: Push + Pull model.

## optimize 'Like' info

In tweet table, if we need to count(user) who liked, it's gonna take forever.

**We must denormalize this data**!

![](/images/jiuzhang-denormalize.png)

Denormalize: it's duplicate info but we store in table, because of performance improvement.

**Shortcoming: inconsistency**!

1. unless using SQL transaction, async failure can result in wrong counting number
2. race condition

Solution: 1. use atomic operation 2. every day, schedule to update this number.

## optimize thundering herd problem

When cache fails, all DB query will go to DB. This results in DB crash.

Hot spot (thundering herd)

![](/images/jiuzhang-thundering-herd.png)

Solution: hold all incoming queries (who fails cache), and only send 1 DB query. When result is returned, return to every query.

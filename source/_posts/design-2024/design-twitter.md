---
title: System Design 2024 - Twitter
comments: true
category: Design
tags: []
---

# Design Twitter

We'll follow the 5-step procedure:

* Scenario
* Numbers
* API and Database
* Performance
* Evolve

# 1. Scenario

## Functional requirement

1. __tweets__
    1. create
    1. delete
1. __timeline/feeds__
    1. home timeline
    1. user self timeline
1. follow
1. like
1. search

## Non-Functional requirement

The C-A-P theory:

1. Consistency: eventual, no need strong consistency. 

1. Availability: 
    1. always available
    1. no gurantee of most updated data
    1. scaclable, low-latency

1. Partition tolerance
    1. continue to operate despite an arbitrary number of messaged being lost. 

# 2. Numbers

User:

1. DAU = 200M
1. New tweets = 100M per day
1. Each timeline page = 20 tweets
1. Tweet size = 280 bytes, with another 30 bytes of metadata
    1. photo size: 500KB; 20% of tweets have photo
    1. video size = 5MB; 10% of tweets have video, among them 30% will be watched

Data:

1. Write size:
    1. Text
        * 100M * 300Bytes = 30GB
    1. Images
        * 20M * 500KB = 10,000GB
    1. Video
        * 10M * 5MB = 50,000,GB
    1. Total = 60TB of new data every day.
    1. That is 2PB per month. 

1. Bandwidth:
    1. Average user: 5 home visit + 3 profile visit, with each page having 20 tweets
    1. That is 200M * 8visits * 20 = 32 billion tweets/day
    1. Text: 100MB/s
    1. Images: 30GB/s
    1. Video: 50GB/s

why do we need this?

# 3. API and Database

## API design

1. postTweet(token, string)
1. deleteTweet(token, id)
1. likeOrDislike(token, id, bool likeOrDislike)
1. readHomeTimeline(token, int pageSize, string paginationToken)
1. readUserTimeline(token, int pageSize, string paginationToken)

# Application server

## Fan-out on write

Also called "push mode".

For 99% users, when they post a new tweet, write to all their follower's timeline on cache. 

## Fan-in on read

Also called "pull".

This is only efficient for IOLs with >10,000 followers. 

eg. Tylor Swift, Elon Must etc. Only fetch their tweets when user reads. 

# Database

1. User table
    1. id
    1. name
    1. email
    1. isHot: boolean
1. Tweet table
    1. id
    1. creationTime
    1. content: varchar(140)
1. Follower table
    1. userID1: integer
    1. userID2: integer

# 4. Performance

## Scalability

General Steps: 

1. Identify bottleneck
1. Find solutions
    1. data sharding
    1. load balancing
    1. data caching

## Sharding

1. by creation time
    1. Pros: na.
    1. Cons: hot/cold shards
1. by user ID
    1. Pros: simple
    1. Cons: 
        1. need to query many shards for a timeline request (follwer and followee on different shards)
        1. Some IOLs may not fit into 1 shard (non-uniform distribution of storage).
        1. also have hot user issue
1. by hash (tweetId)
    1. Pros: uniform distribution, high availability.
    1. Cons: Need to query all shards. 

# Caching

More read than write. 

Use cache to avoid frequent DB hits. 

Timeline service - is just a pre-computed list of tweet IDs, stored in No-sql DB as a (userId, array<tweets>) K-V pair. This K-V pais is constently updated. 

# 5. Evolve

Follower-followee: try use GraphDB, which is a adjacency list of user relations. 

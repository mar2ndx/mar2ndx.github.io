---
title: System design cheat sheet
comments: true
category: Design
tags: []
---

# Answering framework

    Requirements
        Functional Requirements
        Non-functional requirements
        Out of scope
    Capacity Estimation
        Assumptions
        Storage Estimations
    Detailed Component Design
        Client
        Meta Service
        Block Service
        Notification Service
    Database Schema
    APIs
        Download Chunk
        Upload Chunk
        Get Objects
    Performance
        Chunking Files
        Data Deduplication
        Caching
    Scalability
        Horizontal Scaling
        Database Sharding
        Cache Sharding
    Security
        HTTPS
        Authentication
    Resiliency
        Distributed Block Storage
        Queuing
        Load Balancing
        Geo-redundancy
    References

Other things to remember:

1. uploading file/photo: use master/slave model
1. don't forget to calculate the storage size for DB.
   eg. 500M user data, each take 68 bytes, then storage needed = 32GB
   (user id 4 bytes, name 20 bytes, email 32 bytes, dataofbirth 4 bytes, creation time 4 byte, last login 4 bytes)
1. data sharding - 如果按照 hash 分割，migration 非常困难。
   solution：
   先范围，再 hash。Or 一致性 hash 环（consistent hashing）
1. 如何 generate PhotoID？没有这个 id，我们无法判断哪个 shard。所以：用 snowflake 算法，unique IDs

# 3 most popular AWS services:

1. EC2
1. RDS: support multiple database engines including SQL Server, SQL, PostgreSQL
1. S3: Simple Storage Service (S3)

# Consistent Hashing

Use for data partitioning problem

Dynamo and Cassandra use Consistent Hashing to distribute their data across nodes

# How to ensure API security?

For each API request post log-in, we are doing authentication by checking the validity of auth_token in Authorization HTTP header.

This makes sure that requests which originate from clients are legitimate.

# Facebook big data

Daily = 5 Petabyte = 5,000 Terabyte

ODS = time-series counter

Scube = in-memory

Hive = data warehouse

None of the above are relational DB, thus no ACID properties.

ACID = atomic + consistency + isolation (invisible inter-mediate states) + durability (changes won't undone)

# Kafka

Distributed streaming platform. Support publish-subscibe pattern. Not exactly same as messaging queue.

Use cases:

1. aggregate user activity on a website
1. logs aggregation

# News Feed

pre-generation 然后存入一个 table。

Pull（或者 long-pulling connection）比 Push 更好。

因为：KOL 有 1M follower，push 不过来。但是人可以关注是又上限的：maybe 1000，所以 pull 起来更快一点。

News feed 因为需要快速读写，所以 keep in memory. Eg. 100M users, each required 0.5MB space, then total space needed = 50TB. If each computer = 100GB, we need at least 500 machines.

# Counter service

不能用 Redis 这种 in-memory 来做，除非用户量小于 1000.

用 Kafka + DB 来做。

# Chat app

XMPP protocol over WebSocket (or TCP), it's peer-to-peer

We can't use HTTP which is client-server communication protocol, impossible for chatting app。

## Session Manager

stores user ID - connection ID

so I can find user's websocket, so I know where to send the message

# How does Long polling work?

1. long polling is built on HTTP
1. normally, client send HTTP request and server respond
1. for long-polling, client send the request but server does not close the connection.

The server does not close the connection, instead, the connection is kept open until there is data for the server to send

Once data is received by the client, it immediately makes another HTTP Long-polling request to the server

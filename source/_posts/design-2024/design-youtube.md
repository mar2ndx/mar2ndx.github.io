---
title: System Design 2024 - Youtube
category: Design
tags: []
comments: true
date: 2024-07-29 06:30
---


# Design Youtube

We'll follow the 5-step procedure:

* Scenario

* Numbers

* API and Database
    * [Important] also include HLD schema!

* Performance
    * Sharding and caching

* Evolve

# 1. Scenario

## Functional requirement

1. __Upload video__
1. __Watch video__
1. Comment and like/dislike
1. Search
1. Recommend
1. Detect bots
1. Ads

## Non-Functional requirement

1. High availability
1. Scale: support 1 billion users
1. Favor availability over consistency
1. Minimize latency

# 2. Numbers

1. 500 uploads per second, from 1 billion registered users. 
1. 

# 3. API and Database

## HLD

1. Need LB before the App server
1. Store raw file uploads to Object store, like AWS S3, Google Cloud Storage. 
1. If you use MongoDB, it's a collection of documents, document is a json. 
1. The data is stored de-normalized (contains duplicate info). eg. Each video will also contains the uploader's profile photo information. If user changes his profile photo, the update will be done asynchronously. 
1. Vidoes should be loaded in smaller chunks. 
1. The technology use for deliverying video is called Streaming. 

## API design

1. upload(title, desc, video, userId, etc...)
1. stream(videoId, startTime, etc...)

# Application server

![](/images/system-design-youtube-1.png)

# Database

Skip for now.

# 4. Performance

## How many encoding server do I need?

If 500 uploads per second, we need much more than 500 encoding servers. 

The requests are gonna be handled by the queue. It depends on how long the encoding, and how many thread on each worker. 

Keep checking the backload status on the worker cluster. 

eg. if each encoding cost 1 minutes, and each worker have 4 threads running encoding job. then you need 500 * 60 / 4 = 7,500 workers. 

## TCP or UDP?

Favor UDP over TCP, only if you are doing live-streaming. 

But for youtube, it's actually steaming a fixed video content. It actually send HTTP in smaller chunks, which is built on TCP technology. And it's sending video and audio seperately. 

## NoSQL or MySQL?

Youtube actually uses MySQL.

Later they added read-only NoSQL databse, and added sharding. 

Later they built Vitess, which decouples application layer from DB layer, and scaled up MySQL for their usecase. Tody PlanetScale also uses Vitess. 

# 5. Evolve


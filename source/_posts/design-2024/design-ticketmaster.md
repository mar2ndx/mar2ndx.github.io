---
title: System Design 2024 - TicketMaster
comments: true
category: Design
tags: []
---

# Design TicketMaster

We'll follow the 5-step procedure:

* Scenario

* Numbers

* API and Database
    * [Important] also include HLD schema!

* Performance
    * Sharding and caching.

* Evolve
    * Read some real-world knowledge. 

# 1. Scenario

## Functional requirement

1. Book a ticket
1. View an event
1. Event discovery (search)

## Non-Functional requirement

1. For search and viewing: __High availability__.
1. However for booking, __favor consistency__ over availability (avoid double booking)
1. Scalability: support surges from popular events
1. Minimize latency

### Out of scope:

1. GDPR compliance
1. Fault tolerance


# 2. Numbers

Skip.

# 3. API and Database

## Core entities

1. Event
1. Venue
1. Performer
1. Ticket

## API design

Create an API for each of the functional requirements, and in exchange return entities in your core entities section. 

* GET `/event/:eventId` -> Event & Venue & Performer & Ticket[]
* Get `/search?term={text}&location={lat,long}&type={string}&date={date}` -> Partial<Events>[] 
    * It's inspired by TypeScript, it's perfectly fine to return array of events
* POST `/booking/reserve` -> hold the ticket for 10 minutes
    * Note that booking is a 2-phase process. 
        1. choose a seat (reserve phase)
        1. a timer count-down starts (eg. 10 minutes)
        1. pay within 10 minutes
    * Request example: 
    ```
    header: JWT | sessionToken # this includes user's information.
    body: {
        ticketId
        # Please do not include userId here for security reason, since hacker could alter it
    }
    ```
* POST `/booking/confirm`
    ```
    header: JWT | sessionToken # Never put usre's ID in the request body.
    body: {
        ticketId,
        paymentDetails (eg. for Stripe, there is a PaymentIntents that can be setup in client library),
    }
    ```

## Data Model

1. Event table
1. Venue - seatMap
1. Performer
1. Ticket - seat, price

### Postgres or NoSQL?

Postgres (a SQL database) is easy to use, since it supports Transactions, support SQL queries, supports asset properties on Tickets. 

Well, Amazon's DynamoDB (noSQL) also works. It also supports __asset property__. 

## HLD

![](/images/system-design-ticketmaster-1.png)

### To book a ticket

Option 1 : keep a status column in the ticket table, another column called statusUpdateTime. 

If the status is "available", or status is "reverved" but the statusUpdateTime is >10min ago, that means the ticket is supposed to be released, and can be booked again.

This design is horrible. 

Option 2 : Setup a cron job

This job will periodically update the ticket reserve/book status. 

This is still, not very much real-time. 

Option 3 : Keep a seperate service called "TicketLock", using Redis. 

This is a _Distributed Lock__. 

Instead of modifying our Ticket table, use Redis to keep all reserved ticket, with value like this: {ticketId, true} ttl = 600 seconds. 

After 10 minutes, this K-V pair is automatically deleted from Redis.

Steps: 

1. User request tickets with status = available
1. backend check Redis and remove all tickets that exists in the Redis
1. User request to book ticket 1234
1. add {1234, true} to Redis with ttl=600
1. 10 minutes later without payment confirmation, Redis removes {1234, true}
1. User comes back after 15 minutes, ticket 1234 is still available for booking.

Q: what if the lock goes down?

1. Immediately bring on up
1. Many user will be able to book the system ticket (double book problem).
1. Whoever submitted payment first, will win the ticket. 

# 4. Performance

For performance deep-dive, show off your skills, especially if you are senior/staff level. 

Find 1~3 places where you can optimize. Find from your non-functional requirements section. 

## 4.1 Search with low-latency

Currently: full-table scan. 

```
Select * from DB
Where type in []
AND name like "%term%"
```

This is bad, since the wildcard means I need to do DB-scan on the entire table. 

New solution: ElasticSearch.

1. Build an inverted-index to make searching document by 'terms' really fast. 
1. Tokenize the sets of strings, eg. "Golden state warriors" is a term. 
1. Map this term to the events. like this:
    ```
    playoff: [event1, event2, event3, event4]
    swift: [event45, event134, event93]
    ```
1. ElasticSearch supports Geo-spacial queries as well.
1. You can search a combination of {locations, date, terms} at the same time. 

Note: don't use ElasticSearch as primary DB, learnt it the hard way.

## 4.2 How to sync data between Postgres and ElasticSearch

Option 1 : write to both primary data store, and also ElasticSearch

Not good. Retries happen. 

Option 2 : Change data capture (CDC)

For any updates to Posgres, create a stream of change events, and consumed by ElasticSearch.

There's a limit for number of writes per second. 

## 4.3 Handle popular events?

Caching. 

Option 1 : OpenSearch. 

AWS OpenSearch is a fully-managed ElasticSearch. It supports 'node query caching'. 

It will cache the top 10K queries for each shard on your ElasticSearch cluster, using the Least recently used (LRU) Cache. 

Option 2 : cache <search term, result> K-V into Redis. 

Option 3 : You already got a CDN, cache API called and response. 

eg. people search "taylor swift" a lot, put this result in CDN cache. 

## 4.4 Event Ranking and Reco?

Not covered. 

# 5. Evolve

## SeatMap user experience

Front-end need to keep a HTTP-based long-pull to update seat map in real-time. 

Also, can use bi-directional persistent connection like WebSocket. 

Similarly, open a connection of Server-sent events (SSE). 

Keep difference:

1. WebSocket is bi-directional.
1. SSE is uni-directional. 

## Everyone sees a black map

For super-popular events, every seat is reserved with 1 seconds. 

Introduce a choke-point (essentially, a virtual waiting queue), using Redis. K-V will be like <userId, token>

Basically, before user enters an event page, tell users to "please wait to enter this page". Each time, only allow 100 people book tickets for a single event. 

## How to achive strong consistency?

TicketLock using Redis.

---
title: System Design 2024 - Bidding Platform
comments: true
category: Design
tags: []
---

# Design Bidding Platform

# 1. Requirements

1. A user can bid on an item.
1. Fix-time bidding & Variable-time bidding.
1. Real-time price update.
1. Support 100+ QPS for each item.  

# 2. Data Model

1. Bid表

   bidID, auctionID, userID, price, serverside_timestamp, status. 

   __status__ could be Accepted/Rejected. 

   Put this into a __time-series database__ by autionID, because eventually we need all bids per auction for auditing purposes. 

1. AuctionState表

   autionID, currentWinningBidID, price, end_auction_timestamp.

   This is only 32 bytes, thus entire storage is < 32GB, can use in-memory DB. 

# 3. Bidding Core

* This system is similar to the Robinhood (Stock Exchange) Design. 
* Need a single point of "choke-point". A multi-leader or leaderless model won't work here. 

## Option 1: bid with Kafka

Use Kafka as log-based message broker. 

Order by log. 

Kafka uses Kernel bypass to achieve high write throughput. 

![](/images/system-design-bidding-platform-1.png)

Downside: use will be notified about bidding result, async. Thus using Kafka is not a great solution. 

## Option 2: synchronized-bid

Bid Engine: single choke point. 

It must handle high throughput. 

State-machine replication, similar to the exchange. 



Solution: 

1. In-memory.
2. No disk read or network calls. 
3. For each request, lock the auction state, compare bids, and proceed. 
4. We can partition Bid Engine by auctionID using consistant hashing. 
5. But make sure all bids for 1 auction always on the same machine. 

![](/images/system-design-bidding-platform-2.png)

### How to achieve fault tolerance?

Need a backup, that only listens to master. 

Each bid has a seq number. 

# 4. Message delivery

Multiple clients want to know the bidding results, namely: 

1. Backup bidding engine
2. Audit database
3. Other users

Let's put in Kafka __so multiple consumers can subscribe__! 

Remember your Kafka is the source of truth, with certain replication configurations. 

![](/images/system-design-bidding-platform-3.png)

Note: 

1. Publish to Kafka first, then notify user. 
2. However, it's possible that bid is lost if Kafka goes down, so maybe publish to 2 brokers instead of 1. 

## How to keep Bid Engine thoughput high?

Remember now we have additional network call to Kafka, and we need sychronous return to cleint about the bid result. 

Here's the psueducode. 

![](/images/system-design-bidding-platform-4.png)

But to solve the problem of Kafka race condition: 

![](/images/system-design-bidding-platform-5.png)

这一段没太看懂！



# 5. Bid consumers

![](/images/system-design-bidding-platform-6.png)



# 6. Popular auctions

Many people watching the top Kafka queue. like this:

![](/images/system-design-bidding-platform-7.png)



# 7. Auction ending

1. As bid come in, update the finish time. 
2. Bid engine occasionally check the auction time. 

![](/images/system-design-bidding-platform-8.png)



Reference：https://www.youtube.com/watch?v=3aX-lC5_P1M
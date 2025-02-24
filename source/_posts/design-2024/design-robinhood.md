---
title: System Design 2024 - Robinhood
comments: true
category: Design
tags: []
---

# Requirements

1. User buy/sell financial products via an Exchange.
1. User can check their positions.
1. User sees real-time value of their assets on 1 screen
1. Minimize # of servers that listen to Exchange (this is very costly).

# Numbers

Assume 100 Million users, and 100 instruments in each portfolio. 

Example of instruments:

1. Stock
1. Option

# HLD

## Thoughs

1. It's a phone app, try to limit number of connections per client. 
1. If user have multiple devices, make sure they connect to the same server.
    > consistent hashing to decide which server a userId connects to.
1. Robinhood is an agent, not an exchange. 
1. There could be race condition when user cancel an order. 

## Order Placing Diagram

To place an order:

1. User sent a order request to Order Pending Table.
1. Goes to Order Gateway, place order to Exchange.
1. Map the exchange order ID to robinhood order ID. Let's call it Order Mapping Table. 
1. Listener cluster will listen to exchange, and update Order Table once there is a filled order. 

To cancel an order:

1. User send request to Order Gateway, get exchange order ID. 
1. Use the exchange order ID to cancel order
1. ONLY notify users once the exchange cancellation is successful. 

## HLD

![](/images/system-design-robinhood-1.jpg)

## What is "price"? 

1. Trade price is determined by combination of bid/ask prices.
    1. Last trade price
    1. Take highest buy price & lowest sell price, average from multiple exchanges. 
    1. Volume-weighted average price.

## Read Positions

Need to get user's position, and each stock's price. 

For position: use the Orders Table to create Positions Table using derived data, change data capture, have kafka consumer, and update total positions. 

For pricing, we should not let User Service to connect to Exchange directly, since its too costly. 

# Delivering Pricing to User

## Exchange Layer

Publish pricing through UDP. We want this layer as small as possible. 

## Pricing Layer

1. Decide a price for each assets based on imcoming data from multiple exchanges
1. Deliver prices to user layer (through WebSocket)

The price is decided by multiple algorithms:

1. Last trade price
1. Some form of stateful calculation: 
    1. moving average
    1. active bids/asks

Need to do a state machine replication to make sure pricing layer is fault-tolerance. Zookeeper can help with fail-over. 

We can shard the data on hashing of the ticker. 

### Some Stock are Super-hot

A pricing server can be overloaded by either:

1. too many data from one exchange
1. too many user to check price on a certain stock

Solution:

1. Only publish the average of the last 10 trades. 
1. Price over the aggregation of open bids and asks. 
    1. Either exchange layer aggregate the data
    1. Or send over the snapshot of orderbook to pricing layer, and pricing layer aggregate. 

### Re-sharding

TODO

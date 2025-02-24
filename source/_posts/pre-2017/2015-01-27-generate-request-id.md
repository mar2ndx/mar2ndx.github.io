---
layout: post
title: "[Google] Generate Request ID "
comments: true
category: q-google
---

### Question

[link](http://www.careercup.com/question?id=5169800024162304)

> Design a system to **return an unique ID for each request**.

> (For most of requests, the ID value should increase as time goes, the system should handle 1000 requests per second at least. )

> Note: **Timestamps** alone is not valid since there might be multiple requests with same timestamps.

### Idea 1

#### Generating UUID

**A universally unique identifier (UUID)** is an identifier standard used in software construction. A UUID is simply a 128-bit value.

Generating unique IDs is easy. All modern OS'es have that functionality built in.

**Detail**: UUIDs may be generated from a combination of **system time stamp, CPU/system ID**, NIC MAC addresses, HBA WWNs, server id etc.

#### Clarifications

Let's assume the following:

1. What's the length of the ID?

   <= 128 bits. In that case I'll choose the standard 128 bit UUID format.

1. The requirement states the system should handle 1000 request/s at least.

1. What's the average request rate?

   1000 < avg req. rate < 10,000

1. What's the max. burst rate the system must handle?

   < 1,000,000

1. What's the max. latency (wait time) for a request?

   1 ms

#### Solution

It's a classical consumer-producer problem.

In this case we have many consumers of UUIDs and one producer. Let's assume the OS provides an API to generate UUIDs and the max. running time of the API is 1ms.

1. Pre-allocate 2 Mio UUIDs into an array / stack/ heap (depending on implementation) structure.

1. If no overhead 2 Mio UUIDs would take ~ 32MB of RAM. Not a problem on today's server system with many GB of RAM, but may be a problem on an embedded system.

1. 2 Mio UUIDs ensures system can handle burst rate.

1. The solution needs to ensure that its pool of UUIDs doesn't run out as consumers request them and they are replenished.

### Idea 2

This question is quite open-ended.

For starter, how about **appending random(N) to the timestamp**? N can be large enough to make collisions unlikely. If each server has an ID we can also include it to further reduce collisions.

If IDs must be unique, then I suppose you can **design a counter** that will return an ID and increment it at the same time. You will then **need mutex to access this counter**.

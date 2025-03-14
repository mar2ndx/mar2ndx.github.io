---
title: "[CC150v5] 8.7 Design Online Chat Server (2)"
category: CC150v5
tags: []
comments: true
date: 2014-08-24 00:00
---


... Continued from previous post.

### Overall view

The system consists of a database, a set of clients, and a set of servers. This is not about OOD, but we need to know.

1. DB stores user list, chat archive. An SQL DB would be good, **unless we want BigTable for scalability purpose**.

1. **We use XML for server-client communication**. Because it's debugging friendly.

1. **A set of servers**.

   1. Data will be **divided up across machines**, requiring us to potentially hop from machine to machine.
   1. When possible, we will try to **replicate some data** across machines to minimize the lookups.
   1. One major design constraint here is to **prevent having a single point of failure**. For instance, if one machine controlled all the user sign-ins, then we'd cut off millions of users potentially if a single machine lost network connectivity.

### Hardest problems

Or the most interesting questions.

#### Q1: How do we know if someone is online?

While we would like users to tell us when they sign off, we can't know for sure. A user's connection might have died, for example. To make sure that we know when a user has signed off, we might try regularly pinging the client to make sure it's still there.

#### Q2: How do we deal with conflicting information?

We have some information stored in the computer's memory and some in the database. What happens if they get out of sync? Which one is "right"?

#### Q3: How do we make our server scale?

While we designed out chat server without worrying—too much- about scalability, in real life this would be a concern. We'd need to split our data across many servers, which would increase our concern about out-of-sync data.

#### Q4: How we do prevent denial of service attacks?

Clients can push data to us —- what if they try to DOS (denial of service) us? How do we prevent that?

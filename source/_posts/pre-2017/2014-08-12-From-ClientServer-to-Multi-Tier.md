---
title: "[Design] From Client/Server to Multi-Tier"
category: Design
tags: []
comments: true
date: 2014-08-12 00:00
---


### Client/Server

[link](http://wiki.remobjects.com/wiki/From_Client/Server_to_Multi-Tier)

Client have **direct and full access to the physical database** based on their login string. This is the major weakness of the Client/Server paradigm. The system is vulnerable to attacks.

Because all business logic was **implemented on the client application**, changes to business logic means redeploying new client software to all users again.

Another drawback is that the network interface provided by most back-end database systems has been designed for access over the local network, using fast connections and no firewalls. Nowadays, many clients’ software needs to run from employee's home offices or from airport lounges. In many cases such connections **will be unreliable or inefficient** to work on.

### Multi-Tier

The communication between clients and middle-tier server is **no longer tied to a protocol dictated by the database** (no database drivers or connection string on the client). Client applications can authenticate with **a username and password (compare to login string)**.

Communication can be done via HTTP or HTTPS, alternatively or additionally, open standards such as **SOAP, OData and JSON can be used to expose a middle tier** to different clients using protocols that are widely understood.

Biggest advantage is that **all the business logic is transferred from client application into the middle tier**. And the middle tier holds the final control over what data goes in or out.

Still, there're still some business logic on the client tier as well. But it only **complement the rules** that are enforced on the server. Eg. Twitter enforce the 140 character limit locally, and stop you from sending a tweet that is too long (by graying out the Send button).

That means, client side checks are for convenience, and for convenience only; the middle tier server is and must be authoritative for what is allowed and what is not.

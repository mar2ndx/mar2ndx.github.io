---
title: "[Design] P2P Technology "
category: Design
tags: []
comments: true
date: 2015-01-07 00:00
---


### Overview

**[Peer-to-peer](http://en.wikipedia.org/wiki/Peer-to-peer) (P2P) networking** is a distributed application architecture that partitions tasks or work loads between peers.

Peers are **both suppliers and consumers** of resources, in contrast to the traditional client-server model where communication is usually to and from a central server. A typical example of a file transfer that uses the client-server model is the **File Transfer Protocol** (FTP) service in which the client and server programs are distinct: the clients initiate the transfer, and the servers satisfy these requests.

This architecture was popularized by the file sharing system Napster, originally released in 1999.

#### Precedure

1. Alice run P2P client software.
   1. connect to Internet and get new IP address for each connection
   1. register her files in P2P system
   1. request "Harry Potter"
   1. find other peers who have the copy
   1. choose one and copy to her PC.
   1. meanwhile, Alice is servig her files for other people
1. Act like a server
1. Act like a client
1. User keyword to search content (like google)

### P2P Types

1. Unstructured P2P: **no coupling between nodes and file location**
   1. Napster
   1. Gnutella
   1. KaZaA
1. Structured P2P: **tight coupling between nodes and file location**
   1. DHT

#### Napster

Register at Napster server.

Centralized search, and P2P distributing.

#### Gnutella

**Decentralized** design for searching:

1. No central directory server
1. Each node maintain a list of neighbors (overlay network)

**Search by flooding**:

1. BFS traversal.
1. Define maximum number of hops
1. Expanded-ring TTL search means to try 1 hop first, then try 2 hops, then 3...

Join nodes:

1. Use Bootstrap node to get some IP addresses
1. Join these IP, which becomes neighbors.

Shortcomings:

1. Flooding is **NOT a scalable design**.
1. Download may not complete.
1. Possibility of search failure, even then the resource presents.

#### KaZaA

Combines Napster and Gnutella.

Each peer is a supernode or assigned to a supernode. Each supernode connects to 30~50 other supernodes. The supernode acts like a mini-Napster hub.

At registration, a PC connects to a supernode. If a supernode goes down, obtains updated list and elect another one.

Search within supernode, then in other supernodes. If found many nodes holding the file, do parallel downloading.

Automatic recovery if 1 server peer goes down. Use **ContentHash** to search.

#### Structured P2P

For Distributed HashTable services, refer to **[Design] Distributed hash table**.

### Conclusion

1. Unstructured P2P:

   1. **no coupling between nodes and file location**
   1. Centralized direcotry service (except Gnutella)
   1. Search by flooding (overhead)
   1. Hierarchical architecture (non-scalable)

1. Structured P2P:
   1. **tight coupling between nodes and file location**
   1. DHT using consistent hashing (eg. Chord, and many other types)
   1. A node is assigned to hold particular content
   1. Search with more efficiency

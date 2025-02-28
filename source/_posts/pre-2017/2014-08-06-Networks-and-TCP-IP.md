---
title: "[Design] Networks and TCP/IP"
category: Design
tags: []
comments: true
date: 2014-08-06 00:00
---


## Overview

**[Internet protocol suite](http://en.wikipedia.org/wiki/Internet_protocol_suite)** is a networking model and communications protocols used by the Internet. It is commonly known as **TCP/IP**.

Four abstraction layers:

1. Application layer
1. Transport layer
1. Internet layer
1. Link layer

![](/images/network-layers-connected.png)

The protocols are maintained by the **Internet Engineering Task Force** (IETF).

### A summary of four-layer model

1. Application: authentication, compression, and end user services
1. Transport: handles the flow of data between systems and provides access to the network for applications via the BSD socket library
1. Network: packet routing
1. Link: Kernel OS/device driver interface to the network interface on the computer.

[source](http://searchnetworking.techtarget.com/news/851291/TCP-Internet-Protocol-and-OSI)

### More details

**The Application layer**:

1. where applications create user data and communicate with other applications on another host (make use of Transport Layer to provide reliable or unreliable pipes to other processes).
1. different application architecture, such as the client-server model and peer-to-peer.
1. SMTP, FTP, SSH, HTTP all operate above this layer.
1. processes are addressed via ports.

![](/images/network-ports.gif)

> Well-known official port numbers are in the range of 0 - 255. Port 256 - 1023 are reserved for other well-known services. 1024 - 65535 are neither in-use nor reserved. They are used when TCP/IP automatically assigns port numbers to client programs.

**The Transport Layer**:

1. performs host-to-host communications.
1. "UDP" provides unreliable datagram service.
1. "**Transmission Control Protocol**" provides flow-control, connection establishment, and reliable transmission of data.

**The Internet layer**:

1. exchange datagrams across network boundaries.
1. establishes internetworking thus establishes the Internet.
1. "**Internet Protocol**", defines IP addresses and the routing structures used for the TCP/IP protocol suite.
1. routing: transport datagrams to the next IP router that has the connectivity to a network closer to the final data destination.

**The Link layer**:

1. defines the networking methods within local network link without intervening routers.
1. describe local network topology and the interfaces needed to effect transmission of Internet layer datagrams to next-neighbor hosts.

### Difference from OSI

The Internet protocol suite was in use **before the OSI model**, and is well established worldwide.

[The OSI model](http://electronicdesign.com/what-s-difference-between/what-s-difference-between-osi-seven-layer-network-model-and-tcpip), however, is a proven concept that is used in all other data communications protocols. It will continue to be used as a guideline for all other communications applications.

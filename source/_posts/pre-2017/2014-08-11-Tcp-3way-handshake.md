---
title: "[Design] TCP 3-Way Handshake"
category: Design
tags: []
comments: true
date: 2014-08-11 00:00
---


### Handshaking

**[Handshaking](http://en.wikipedia.org/wiki/Handshaking) is an automated process of negotiation** that dynamically sets parameters of a communications channel established between two entities before normal communication over the channel begins.

It is usually a process that takes place when a computer is about to communicate with a foreign device to establish rules for communication.

### TCP three-way handshake

**[TCP three-way handshake](http://www.inetdaemon.com/tutorials/internet/tcp/3-way_handshake.shtml)** is the method used by TCP set up a TCP/IP connection over an Internet Protocol based network.

It's commonly referred to as "**SYN-SYN-ACK**".

![](/images/3way-Tcp-handshake.png)

### Process

1. Host A sends a TCP **SYN**chronize packet to Host B
1. Host B receives A's SYN
1. Host B sends a **SYN**chronize-**ACK**nowledgement
1. Host A receives B's SYN-ACK
1. Host A sends **ACK**nowledge
1. Host B receives ACK.
1. TCP socket connection is ESTABLISHED.

Alternatively, there's a good illustration on [wiki](http://en.wikipedia.org/wiki/Handshaking):

> Establishing a normal TCP connection requires three separate steps:

> 1. The first host (Alice) sends the second host (Bob) a "synchronize" (SYN) message with its own sequence number x, which Bob receives.
>
> 1. Bob replies with a synchronize-acknowledgment (SYN-ACK) message with its own sequence number y and acknowledgement number x + 1, which Alice receives.
>
> 1. Alice replies with an acknowledgment message with acknowledgement number y + 1, which Bob receives and to which he doesn't need to reply.

### Two more thing

Note that **FTP, Telnet, HTTP, HTTPS, SMTP, POP3, IMAP, SSH** and any other protocol that rides over TCP **also has a three way handshake** performed as connection is opened.

TCP 'rides' on top of Internet Protocol (IP) in the protocol stack. IP handles **IP addressing and routing** and gets the packets from one place to another, but TCP manages the **actual communication sockets** between endpoints.

---
title: Service-Oriented Architecture, SOAP and REST
category: unknown
tags: []
comments: true
date: 2025-03-04 00:52:59
---

> SOA protocols like SOAP, WSDL, and WS-* were specifically created to facilitate web services communication using XML-based messaging, ensuring interoperability and standardization across disparate systems.

# Service-Oriented Architecture

SOA protocols were developed in early 2000s to enable standardized, platform-independent communication between different software systems over the internet.

It concludes:

1. SOAP
  ○ Uses XML as its message format.
  ○ Supports RPC.
2. WSDL
  ○ Web Services Description Language
3. WS-Specifications
  ○ WS-Security
  ○ WS-ReliableMessaging
  ○ WS-Transaction
  ○ WS-Addressing

## Deprecation

While SOAP and XML-based web services were groundbreaking in their time, they've largely been superseded by __more agile and lightweight communication protocols__.

With the rise of REST (Representational State Transfer) and JSON-based APIs, SOAP and WS-* protocols have seen decreased adoption. Modern web services typically prefer:

● Lightweight JSON communication
● RESTful architectural principles
● Simpler, more performant API designs

# REST

1、Lightweight JSON Communication

JSON (JavaScript Object Notation) revolutionized web service communication by providing a lightweight, human-readable data exchange format:

● Syntax: Lightweight, text-based format using key-value pairs and arrays
● Data Types: Supports strings, numbers, booleans, null, objects, and arrays
● Parsing: Extremely fast and simple to parse across multiple programming languages
● Size: Significantly smaller compared to XML, reducing bandwidth and processing overhead

2、RESTful Architectural

● Stateless Communication: Each request contains all necessary information
● Client-Server Separation: Clear distinction between client and server responsibilities
● Uniform Interface: Standardized way of interacting with resources
● Cacheable Responses: Ability to cache responses for improved performance
● Layered System: Multiple layers can exist between client and server

3、Modern API design

Performance Optimization:

● Minimal payload size
● Quick serialization and deserialization
● Efficient data transfer
● Reduced network overhead

Design Best Practices:

● Versioning: Built-in API versioning
● Rate Limiting: Control API access frequency
● Authentication: Token-based security mechanisms
● Pagination: Efficient data retrieval for large datasets

## Other Modern Techniques:

● GraphQL: Flexible query language allowing precise data retrieval
● WebSocket: Real-time, bidirectional communication
● gRPC: High-performance RPC framework using Protocol Buffers

---
title: "[Design] Design Cache System (`)"
category: Design
tags: []
comments: true
date: 2015-02-10 00:00
---


### Easy version

[Q] Design a layer **in front of a system** which cache the last n requests and the responses to them from the system.

**[Solution](http://blog.csdn.net/hexinuaa/article/details/6630384)**:

[a] When a request comes look it up in the cache and if it hits then return the response from here and do not pass the request to the system

[b] If the request is not found in the cache then pass it on to the system

[c] Since cache can only store the last n requests, Insert the n+1th request in the cache and delete one of the older requests from the cache

[d]Design one cache such that all operations can be done in O(1) – lookup, delete and insert.

### Distributed Cache

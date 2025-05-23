---
title: "[CC150v4] 11.2 Random error debugging 2 "
category: CC150v4
tags: []
comments: true
date: 2014-09-08 00:00
---


### Question

> You are given the source to an application which crashes when it is run After running it ten times in a debugger, you find it never crashes in the same place The application is single threaded, and uses only the C standard library What programming errors could be causing this crash? How would you test each one?

### Solution

The solution is from **both CC150v4 and CC150v5**. My previous post **[Testing] Random error debugging 1** already covered this question.

Again, the answer is very similar:

1. Depends on random variable
   1. RNG
   1. depends on user input
   1. depends on system date/time
1. Uninitialized variable
   1. can take on arbitrary value
   1. can execute in different path
1. Memory Leak
   1. out of RAM
   1. heap overflow
   1. stack data corruption
1. System Dependency
   1. depends on external module
   1. depends on some system attributed that's being modified by another application (this is especially for hardware-facing applications)

In general, **Web server is more prone to Memory Leak**, and program that runs **close to system level** is more prone to system dependency errors.

Additionally, we may be able to use tools to check for specific situations. For example, to investigate issue #2, we can **utilize runtime tools which check for uninitialized variables**.

---
title: "[Design] Semaphore Mutex Toilet Example"
category: Design
tags: []
comments: true
date: 2014-07-25 00:00
---


## Mutex vs. Semaphore

**Mutex is a [key to a toilet](http://koti.mbnet.fi/niclasw/MutexSemaphore.html)**. One person can have the key - occupy the toilet. When finished, the person gives (frees) the key to the next person in queue.

A mutex is really a semaphore with value 1.

**Semaphore is the number of free identical toilet keys**. Example, say we have four toilets with identical locks and keys. The semaphore count is set to 4 at beginning, then the count decrease as people are coming in, etc.

### A mutex is not a binary semaphore

**A mutex is [locking mechanism](http://www.geeksforgeeks.org/mutex-vs-semaphore/)** used to synchronize access to a resource. Only one task can acquire the mutex.

It means there will be ownership associated with mutex, and only the owner can release the lock.

**Semaphore is signaling mechanism** ("I am done, you can carry on" kind of signal).

For example, if you are listening songs (assume it as one task) on your mobile and at the same time your friend called you, an interrupt will be triggered upon which an interrupt service routine (ISR) will signal the call processing task to wakeup.

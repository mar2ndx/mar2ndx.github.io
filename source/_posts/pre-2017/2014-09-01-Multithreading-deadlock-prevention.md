---
title: "[Design] Multithreading - Deadlock Prevention "
category: Design
tags: []
comments: true
date: 2014-09-01 00:00
---


### Question

> How to prevent deadlock? (question from MIT handouts 1)

### Analysis

Preventing one of the 4 conditions will prevent deadlock:

1. Removing the **mutual exclusion condition**, but not very possible.

1. The **hold and wait** conditions may be removed by requiring processes to request all the resources they will need before starting up.

1. The **no preemption condition** may also be difficult or impossible to avoid as a process has to be able to have a resource for a certain amount of time, or the processing outcome may be inconsistent or thrashing may occur.

1. The final condition is the **circular wait condition**. Approaches that avoid circular waits include disabling interrupts during critical sections and using a hierarchy to determine a partial ordering of resources.

### Answer

**Assign an order to our locks** (require that the locks always acquired in order).

This prevent 2 thread waiting to get the resource in each other's hand.

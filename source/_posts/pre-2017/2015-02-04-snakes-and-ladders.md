---
title: "[Google] Snakes and ladders "
category: q-google
tags: []
comments: true
date: 2015-02-04 00:00
---


### Question

[link](http://www.careercup.com/question?id=14955106)

> Given a board of snakes and ladders game, provide an algorithm to find the minimum number of dice rolls required to reach 100 from 1.

### Solution 1

Recommended: **Graph (shortest path)**. [ref](http://www.careercup.com/question?id=14955106):

1. k is linked to k + 1 k + 2, k + 3, k + 4, k + 5, k +6.

2. If has a ladder, connect it too.

3. Find shortest path.

Solution 2 is **DP**.

### Variant

If the question asks: find the way to climb as many ladder as possible. Then this question would be solved differently.

Any ideas?

Solution below.

...

...

...

Read **[Greedy] Activity Selection Problem**.

### Code

not written

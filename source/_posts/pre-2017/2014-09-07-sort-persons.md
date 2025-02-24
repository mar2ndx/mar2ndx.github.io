---
layout: post
title: "[CC150v4] 9.0 Example - Sort Persons "
comments: true
category: CC150v4
---

### Question

> You have a very large array of ‘Person’ objects. Sort the people in increasing order of age.

### Solution

First we look at the nature of this question:

1. large input array
1. sort based on age (**which is between 1 and 100**, this is important)

**This exactly matches the charasteristics of Bucket Sort**. Time complexity in average case is O(n + k) where k is the number of buckets.

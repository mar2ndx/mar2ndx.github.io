---
title: "[Question] Check Power of 2"
category: Question
tags: []
comments: true
date: 2014-07-04 00:00
---


### Question

> Requirement: O(1) time

### Solution

Do a special handle for input = 0. [source](http://stackoverflow.com/a/600306)

    bool IsPowerOfTwo(ulong x) {
        return (x & (x - 1)) == 0;
    }

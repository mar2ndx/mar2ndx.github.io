---
title: "[Question] Check string with no common letters (Bitmask) "
category: Question
tags: []
comments: true
date: 2015-02-07 00:00
---


### Question

RT. This is a very very common requirements in the area of string manipulation. We want it to be done very efficiently.

### Solution

Normally, we would use a hashmap. However, we can also use **bitmask** or bitmap.

Work for a-z only, we use 1 integer to represent each letter, and set an integer for each string.

We do (mask1 & mask2 == 0) to find no common letters. Read more at this question, **[Google] Max prodcut of strings that have no common char**.

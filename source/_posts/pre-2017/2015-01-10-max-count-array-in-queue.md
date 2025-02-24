---
layout: post
title: "[Google] Maximum Count Array in a Queue "
comments: true
category: q-google
---

### Question

[link1](http://www.mitbbs.com/article_t1/JobHunting/32856675_0_1.html#top)

> 给一个数组 a[n]，令 s[i]为 a[i+1..n-1]中比 a[i]大的数的数量。

> 求最大的 s[i]。要求 O(nlogn)

### Solution

This is very similar question to **[Google] Form a Queue Given Heights**. The idea is to insert elements into BST and count number of larger elements.

Naitive solution can be reached with a list.

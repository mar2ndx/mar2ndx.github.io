---
layout: post
title: "[Design] Big Data - Remove Duplicate Numbers"
comments: true
category: Design
---

### Question

[link](http://blog.csdn.net/v_JULY_v/article/details/6279498)

> 2.5 亿个整数中找出不重复的整数的个数，内存空间不足以容纳这 2.5 亿个整数。

### Analysis

Categorized under **双层桶划分** or **BitMap**.

整数个数为 2^32,也就是，我们可以将这 2^32 个数，划分为 2^8 个区域(比如用单个文件代表一个区域)，然后将数据分离到不同的区域，然后不同的区域在利用 bitmap 就可以直接解决了。

**But how exactly to use BitMap**? 将 bit-map 扩展一下，用 2bit 表示一个数即可，0 表示未出现，1 表示出现一次，2 表示出现 2 次及以上。

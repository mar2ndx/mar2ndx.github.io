---
title: "[Design] Big Data - Find Existence of a Number"
category: Design
tags: []
comments: true
date: 2014-08-10 00:00
---


### Question

[link](http://blog.csdn.net/v_july_v/article/details/7382693)

> 给 40 亿个不重复的 unsigned int 的整数，没排过序的，然后再给一个数，如何快速判断这个数是否在那 40 亿个数当中？

### Analysis

Categorized under **BitMap**.

There're 4.3 billion unsigned integers in Java. This is a perfect question to use BitMap.

申请 512M 的内存，一个 bit 位代表一个 unsigned int 值。读入 40 亿个数，设置相应的 bit 位，读入要查询的数，查看相应 bit 位是否为 1，为 1 表示存在，为 0 表示不存在。

---
title: "[Google] Guess Password "
category: q-google
tags: []
comments: true
date: 2014-09-16 00:00
---


### Question

[link](http://www.mitbbs.com/article_t/JobHunting/32658281.html)

> 给你一个 password 假定 6 位

> 有个 function, 每 call 一次就给你一个 triplet 是 password 里的随即三位(order 不变)。比如 google, 可能返回: ggl, goe, oog, ool...

> 问如何最有效破译这个密码?

### Solution

This is just a rough idea suggested by Level 6 of [this post](http://www.mitbbs.com/article_t/JobHunting/32658281.html).

> 六位密码随机给三位，应该有 C(6, 3) = 20 个 bucket。

> 如果密码是 abcdef，那么以 a 开头的 bucket 应该是 C(5, 2) = 10 个。以 b 开头的 buckt 应该是 C(4, 2) = 6 个，以 c 开头的是 3 个，以 d 开头的是 1 个.... from this, we know the probability of the occurrance of each letter.

In this case, we generate many triplets, and calculate based on their frequencies. However, the guy also wrote about this condition:

> 如果 abcd 中间有相同(there are same letters in the 6-char password)，那么就会出现以 a 开头的是 11 个（abca)，13 个(abad)，14 个(abaa)，16 个(aacd)，17 个(aaca),19 个(aaad)或者 20 个(aaaa).

> 思路是比较清楚，不过算法还要想想。

### Code

**not written**

---
title: "[Question] Fit 1*2 Dominos In 2*N Strip"
category: Question
tags: []
comments: true
date: 2014-07-27 00:00
---


### Question

[link](http://tech-queries.blogspot.sg/2011/07/fit-12-dominos-in-2n-strip.html)

> In how many ways can one tile a 2 X N strip of square cells with 1 X 2 dominos?

![](/images/Dominos.png)

### Solution

**X(n+1) = X(n) + X(n-1)**

It's a Fibonacci Series with X(1) = 1 and X(2) = 2.

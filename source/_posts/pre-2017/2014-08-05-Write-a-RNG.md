---
title: "[Google] Write a Random Number Generator"
category: q-google
tags: []
comments: true
date: 2014-08-05 00:00
---


### Question

[link](http://www.careercup.com/question?id=5173972006076416)

### Solution

Basically, the formula is as follows:

> number = (previous_number \* constant + other_constant) mod third_constant

The three constants are carefully selected, and a typical choice is:

> number = (previous_number \* 214013 + 2531011) mod 2^15

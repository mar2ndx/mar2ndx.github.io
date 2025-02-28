---
title: "[Question] Greatest Common Divisor"
category: Question
tags: []
comments: true
date: 2014-08-15 00:00
---


### Question 

> Get GCD in more efficient code

### Code

this is 掉渣天。

	public int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a % b);
	}

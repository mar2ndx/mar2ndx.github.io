---
title: "[Design] Two's complement (2's complement) "
category: Design
tags: []
comments: true
date: 2014-07-13 00:00
---


# Overview

Two's complement is a binary signed number representation.

Negative values are taken by **subtracting the number from 2^n**. This is the most common method of representing signed integers on computers.

## Example

![](/images/twoscomplement.png)

So basically '1111 1111' means -1, and '1000 0000' means -128.

## Special case

In java, minimum integer = -2147483648, which is "10000000000000000000000000000000". If we negative this value, we still get -2147483648!

    public void solve(int A) {
    	System.out.println(A);
    	System.out.println(Integer.toBinaryString(A));
    	System.out.println(A * -1);
    	System.out.println(Integer.toBinaryString(-1 * A));
    	System.out.println(-A);
    }

We get:

    -2147483648
    10000000000000000000000000000000
    -2147483648
    10000000000000000000000000000000
    -2147483648

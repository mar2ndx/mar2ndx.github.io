---
title: "[CC150v5] 5.6 Swap Odd and Even Bits "
category: CC150v5
tags: []
comments: true
date: 2014-09-16 00:00
---


### Question

> Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

### Solution

Mask odd and even bits seperately.

### Code

    public static int swapOddEvenBits(int x) {
    	return (((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1));
    }

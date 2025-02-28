---
title: "[CC150v5] 2.2 Kth last element (recursive) "
category: CC150v5
tags: []
comments: true
date: 2014-09-14 00:00
---


### Question

> Implement an algorithm to find the kth to last element of a singly linked list.

> Do it recursively.

### Solution

Iterative solution is easy, **recursive is not**.

### Code

    public static int nthToLastRecursive(LinkedListNode head, int n) {
    	if (n == 0 || head == null) {
    		return 0;
    	}
    	int k = nthToLastRecursive(head.next, n) + 1;
    	if (k == n) {
    		System.out.println(n + "th to last node is " + head.data);
    	}
    	return k;
    }

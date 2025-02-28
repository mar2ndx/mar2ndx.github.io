---
title: "[CC150v4] 3.6 Sort Stack"
category: CC150v4
tags: []
comments: true
date: 2014-09-06 00:00
---


### Question

> Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented.

> The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

### Solution

This is a very good question that tests stack operations.

### Code

**written by me**

    public static Stack<Integer> sort(Stack<Integer> s) {
    	Stack<Integer> result = new Stack<Integer>();
    	while (!s.isEmpty()) {
    		Integer nextNum = s.pop();
    		while (!result.isEmpty() && result.peek() < nextNum) {
    			s.push(result.pop());
    		}
    		result.push(nextNum);
    	}
    	return result;
    }

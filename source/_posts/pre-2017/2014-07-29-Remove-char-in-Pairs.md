---
title: "[Question] Remove chars in Pairs"
category: Question
tags: []
comments: true
date: 2014-07-29 00:00
---


### Question

[link](http://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/)

> Given a string, recursively remove adjacent duplicate characters from string. The output string should not have any adjacent duplicates.

> Input: azxxzy
>
> Output: ay
>
> First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, so it is further reduced to "ay".

### Analysis

We could do it recursively until all pairs are removed, but it's not good.

There's an O(n) solution.

### Solution

**Most obvious solution is to use a stack**. In the end, the stack stores all unmatched chars.

But we can also **do it without using space** (assuming the input is char array). Just use the original char array to store result, with the helper of 2 pointers. [The code](http://tech-queries.blogspot.sg/2011/02/remove-pairs.html) is very much concise.

### Code

**Refactored code by me**

    public static String remove_pair(char[] input) {
    	int len = input.length;
    	int right = 1, left = 0;

    	while (right < len) {
    		// Cancel pairs
    		while (right < len && left >= 0 && input[right] == input[left]) {
    			right++;
    			left--;
    		}
    		if (right == len) {
    			break;
    		}
    		input[++left] = input[right++];
    	}
    	return String.valueOf(input).substring(0, left + 1);
    }

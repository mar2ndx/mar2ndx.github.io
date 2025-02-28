---
title: "[Google] String Replacement Question "
category: q-google
tags: []
comments: true
date: 2014-09-03 00:00
---


### Question

[link](http://www.mitbbs.com/article_t/JobHunting/32766461.html)

> String replace, 给一个原 string，一个 target，一个替换的新 str，把所有出现
> target str 的地方都换成新的 str， 长度可以任意.

### Solution

If the question asks for an in-place algo, then we can refer to **Question 1.5 in CC150v4**.

### Question

> 1.5 Write a method to replace all spaces in a string with ‘%20’.

### Solution

1. **pre-processing**, count the number of spaces in string
2. parse the string from end to beginning.

Need 2 pass.

### Code

**not written by me**

    public static void ReplaceFun(char[] str, int length) {
    	int spaceCount = 0, newLength, i = 0;
    	for (i = 0; i < length; i++) {
    		if (str[i] == ' ') {
    			spaceCount++;
    		}
    	}
    	newLength = length + spaceCount * 2;
    	str[newLength] = '\0';
    	for (i = length - 1; i >= 0; i--) {
    		if (str[i] == ' ') {
    			str[newLength - 1] = '0';
    			str[newLength - 2] = '2';
    			str[newLength - 3] = '%';
    			newLength = newLength - 3;
    		} else {
    			str[newLength - 1] = str[i];
    			newLength = newLength - 1;
    		}
    	}
    }

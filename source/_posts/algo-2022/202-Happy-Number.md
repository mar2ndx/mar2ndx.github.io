---
title: 202. Happy Number
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/happy-number/

# Question

difficulty: easy
adj diff: 3

    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    	Starting with any positive integer, replace the number by the sum of the squares of its digits.
    	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    	Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    Example 1:

    Input: n = 19
    Output: true
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

    Example 2:

    Input: n = 2
    Output: false
    Constraints:

    	1 <= n <= 231 - 1

注意避免数字循环（用记忆性搜索）。

# Code

```
    public boolean isHappy(int n) {
        return isHappy(new HashSet<Integer>(), n);
    }

    private boolean isHappy(Set<Integer> set, int n) {
        if (n == 1) return true;
        if (set.contains(n)) return false;
        set.add(n);
        int sum = 0;
        while (n != 0) {
            sum += (n % 10) * (n % 10);
            n /= 10;
        }
        return isHappy(set, sum);
    }
```

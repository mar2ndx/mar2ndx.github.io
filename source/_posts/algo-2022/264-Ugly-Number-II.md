---
title: 264. Ugly Number II
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---



Link: https://leetcode.cn/problems/ugly-number-ii/

# Question

difficulty: mid
adj diff: 4

    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return the nth ugly number.

    Example 1:

    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    Example 2:

    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

    Constraints:

    1 <= n <= 1690

# Code

```
    public int nthUglyNumber(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        int p2 = 1;
        int p3 = 1;
        int p5 = 1;

        for (int i = 2; i <= n; i++) {
            int nextUgly = Math.min(Math.min(dp[p2] * 2, dp[p3] * 3), dp[p5] * 5);
            dp[i] = nextUgly;
            if (dp[p2] * 2 == nextUgly) {
                p2++;
            }
            if (dp[p3] * 3 == nextUgly) {
                p3++;
            }
            if (dp[p5] * 5 == nextUgly) {
                p5++;
            }
        }
        return dp[n];
    }
```

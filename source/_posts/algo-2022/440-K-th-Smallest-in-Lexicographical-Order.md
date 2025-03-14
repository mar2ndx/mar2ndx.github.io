---
title: 440. K-th Smallest in Lexicographical Order
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/

# Question

difficulty: hard
adj diff: 5

    Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
    Example 1:

    Input: n = 13, k = 2
    Output: 10
    Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

    Example 2:

    Input: n = 1, k = 1
    Output: 1
    Constraints:

    	1 <= k <= n <= 109

太难了，不会写。

# Code

```
    public int findKthNumber(int n, int k) {
        int prefix = 1;
        while (k > 1) {
            // eg. if n = 378, then:
            // eg. prefix = 1, 2, 3, 30, 300....
            int curStep = getCount(prefix, n);
            if (curStep < k) {
                k -= curStep;
                prefix++;
            } else {
                prefix *= 10;
                k--;
            }
        }
        return prefix;
    }

    private int getCount(int prefix, long n) {
        int count = 0;
        long min = prefix; // eg. min = 2
        long max = prefix; // eg. max = 2
        while (min <= n) {
            if (max <= n) {
                count += max - min + 1;
            } else {
                count += n - min + 1;
            }
            min = min * 10; // eg. min = 20, or 200
            max = max * 10 + 9; // eg. max = 29, or 299
        }
        return count;
    }
```

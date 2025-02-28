---
title: 1326. Minimum Number of Taps to Open to Water a Garden
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/

# Question

difficulty: hard
adj diff: 5

    There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

    There are n + 1 taps located at points [0, 1, ..., n] in the garden.

    Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

    Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
    Example 1:

    Input: n = 5, ranges = [3,4,1,1,0,0]
    Output: 1
    Explanation: The tap at point 0 can cover the interval [-3,3]
    The tap at point 1 can cover the interval [-3,5]
    The tap at point 2 can cover the interval [1,3]
    The tap at point 3 can cover the interval [2,4]
    The tap at point 4 can cover the interval [4,4]
    The tap at point 5 can cover the interval [5,5]
    Opening Only the second tap will water the whole garden [0,5]

    Example 2:

    Input: n = 3, ranges = [0,0,0,0]
    Output: -1
    Explanation: Even if you activate all the four taps you cannot water the whole garden.
    Constraints:

    	1 <= n <= 104
    	ranges.length == n + 1
    	0 <= ranges[i] <= 100

## Explan

这道题很难。

这个 dp 方程，基本是这个意思：

dp[i]指的是：能 reach 到 i 的所有 tap 之中，最远最远能 reach 到哪个 position？假如是 w，则记录为：

    dp[i] = w

最后，判断有几个不同的 w 值，就行了。

    ranges[] = {3, 0, 0, 0};
    maxReach[] = {3, 3, 3, 0};
    return 1;

# Code

```
    public int minTaps(int n, int[] ranges) {
        int[] maxReach = new int[n + 1];
        // maxReach[i] = w, means that:
        // Pick a tap that could reach position i,
        // it could also (for the max) reach position w.
        for (int i = 0; i <= n; i++) {
            int leftBound = Math.max(0, i - ranges[i]);
            int rightBound = Math.min(n, i + ranges[i]);
            // be careful: j < rightBound, not j <= rightBound
            // because a tap can reach position rightBound,
            // doesn't mean it can cover the area right side of rightBound
            // thus maxReach[rightBound] is still 0
            for (int j = leftBound; j < rightBound; j++) {
                maxReach[j] = Math.max(maxReach[j], rightBound);
            }
        }
        int start = 0;
        int steps = 0;
        while (start < n) {
            if (maxReach[start] == 0) {
                return -1;
            }
            // eg. ranges[] = {3, 0, 0, 0}
            // maxReach[] = {3, 3, 3, 0}, then return 1
            start = maxReach[start];
            steps++;
        }
        return steps;
    }
```

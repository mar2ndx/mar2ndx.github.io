---
title: 276. Paint Fence
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/paint-fence/

# Question

difficulty: mid
adj diff: 4

    You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

    Every post must be painted exactly one color.
    There cannot be three or more consecutive posts with the same color.
    Given the two integers n and k, return the number of ways you can paint the fence.

    Example 1:
    Input: n = 3, k = 2
    Output: 6
    Explanation: All the possibilities are shown.
    Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
    Example 2:

    Input: n = 1, k = 1
    Output: 1
    Example 3:

    Input: n = 7, k = 2
    Output: 42

    Constraints:

    1 <= n <= 50
    1 <= k <= 105
    The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.

这是一道很难的 DP 题，虽然代码并不多。

解释如下：

    定义 f[n] 表示 n 个栅栏时的总方案数。

    1、当 n 为 1 时，上色方案数为 f[1] = k；

    2、当 n 为 2 时，第 2 个栅栏的颜色可以和第 1 个一样，也可以不一样，因此总共有 f[2] = f[1] ×
    k = k × k 个方案数；

    3、当 n > 3 时，给第 n 个栅栏上色时，有两种选择：

    3.1 和上一个不同颜色，那么此时第 n 个可以选的颜色有 k-1 个，截至到 n-1 的方案数为 f[n-1]，于是此时的方案总数为：f[n-1] × (k-1)

    3.2 和上一个相同颜色，那么上一个就不能和上上一个同色，第 n 个可以选的颜色有 k-1 个，第 n-1 个可以选的颜色只有一个，那就是和第 n 个一样的那个，因此截至 n-1 的方案数为 f[n-2] × 1，于是此时的方案总数为：f[n-2] × 1 × (k-1)；

    3.3 合计两个情况，给 n 个栅栏上色总共有 f[n] = f[n - 1] × (k - 1) + f[n - 2] × (k - 1)

# Code

```
    public int numWays(int n, int k) {
        if (n <= 1) {
            return k * n;
        }
        int[] dp = new int[n];
        dp[0] = k;
        dp[1] = k * k;
        for (int i = 2; i < n; i++) {
            dp[i] = (dp[i-2] + dp[i-1]) * (k-1);
        }
        return dp[n - 1];
    }
```

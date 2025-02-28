---
title: 221. Maximal Square
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---



Link: https://leetcode.cn/problems/maximal-square/

# Question

difficulty: mid
adj diff: 3

    Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example 1:

    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4

    Example 2:

    Input: matrix = [["0","1"],["1","0"]]
    Output: 1

    Example 3:

    Input: matrix = [["0"]]
    Output: 0

    Constraints:

    	m == matrix.length
    	n == matrix[i].length
    	1 <= m, n <= 300
    	matrix[i][j] is '0' or '1'.

这道题的重点是 **dp 状态转移方程** 怎么写：

如下：

    dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1

一个例子，如下。

    0 1 1 1 0
    1 1 1 1 0
    0 1 1 1 1
    0 1 1 1 1
    0 0 1 1 1

对应的 dp 值如下。

    0 1 1 1 0
    1 1 2 2 0
    0 1 2 3 1
    0 1 2 3 2
    0 0 1 2 3

# Code

```
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] ans = new int[m][n];
        int max = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '0') {
                    ans[i][j] = 0;
                } else if (i == 0 || j == 0) {
                    ans[i][j] = 1;
                } else {
                    ans[i][j] = Math.min(Math.min(ans[i-1][j], ans[i][j-1]), ans[i-1][j-1]) + 1;
                }
                max = Math.max(max, ans[i][j]);
            }
        }
        return max * max;
    }
```

---
title: 311. Sparse Matrix Multiplication
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/sparse-matrix-multiplication/

# Question

difficulty: mid
adj diff: 3

    Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

    Example 1:

    Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    Output: [[7,0,0],[-7,0,3]]
    Example 2:

    Input: mat1 = [[0]], mat2 = [[0]]
    Output: [[0]]

    Constraints:

    m == mat1.length
    k == mat1[i].length == mat2.length
    n == mat2[i].length
    1 <= m, n, k <= 100
    -100 <= mat1[i][j], mat2[i][j] <= 100

# Code

```
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length;
        int k = mat2.length;
        int n = mat2[0].length;
        int[][] ans = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // ans[i][j] = multiply mat1[i] with mat2 column j
                ans[i][j] = 0;
                for (int h = 0; h < k; h++) {
                    ans[i][j] += mat1[i][h] * mat2[h][j];
                }
            }
        }
        return ans;
    }
```

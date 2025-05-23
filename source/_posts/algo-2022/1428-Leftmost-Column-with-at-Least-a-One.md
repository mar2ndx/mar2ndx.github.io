---
title: 1428. Leftmost Column with at Least a One
category: Leetcode
tags: []
comments: true
date: 2022-11-18 06:31
---



Link: https://leetcode.cn/problems/leftmost-column-with-at-least-a-one/

# Question

difficulty: mid
adj diff: 4

    A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

    Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

    You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
    Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

    For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

    Example 1:

    Input: mat = [[0,0],[1,1]]
    Output: 0
    Example 2:

    Input: mat = [[0,0],[0,1]]
    Output: 1
    Example 3:

    Input: mat = [[0,0],[0,0]]
    Output: -1

    Constraints:

    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is either 0 or 1.
    mat[i] is sorted in non-decreasing order.

这道题的难点在于想法。

网友的一句话解法如下：

> 从右下角开始，遇到 1 往左走，遇到 0 往上走
>
> 走到第一行，答案就很显然了。

# Code

```
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> dimension = binaryMatrix.dimensions();
        int x = dimension.get(0) - 1;
        int y = dimension.get(1) - 1;
        while (x >= 0 && y >= 0) {
            int val = binaryMatrix.get(x, y);
            if (val == 0) {
                x--;
            } else if (val == 1) {
                y--;
            }
        }
        return y + 1 == dimension.get(1) ? -1 : y+1;
    }
```

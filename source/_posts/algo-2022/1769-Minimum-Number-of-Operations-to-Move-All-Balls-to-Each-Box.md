---
title: 1769. Minimum Number of Operations to Move All Balls to Each Box
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

# Question

difficulty: mid
adj diff: 4

    You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.

    Example 1:

    Input: boxes = "110"
    Output: [1,1,3]
    Explanation: The answer for each box is as follows:
    1) First box: you will have to move one ball from the second box to the first box in one operation.
    2) Second box: you will have to move one ball from the first box to the second box in one operation.
    3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

    Example 2:

    Input: boxes = "001011"
    Output: [11,8,5,4,3,4]

    Constraints:

    	n == boxes.length
    	1 <= n <= 2000
    	boxes[i] is either '0' or '1'.

这道题这么做。将 array 分成 4 个部分：

    {n1, n2, n3....}, {n(i-1)}, {n(i)}, {n(i+1) .....}

那么这四个部分的 ‘1’ 的数量，分别是：

    leftCount，boxes[i-1], boxes[i], rightCount

那么，dp 方程就是：

    dp[i] = dp[i-1] + leftCount - rightCount + balls[i-1] - balls[i];

# Code

```
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        char[] balls = boxes.toCharArray();
        int leftCount = 0;
        int rightCount = 0;
        int[] dp = new int[n];

        for (int i = 1; i < n; i++) {
            if (balls[i] == '1') {
                rightCount++;
                dp[0] += i;
            }
        }
        for (int i = 1; i < n; i++) {
            if (i > 1 && balls[i - 2] == '1') {
                leftCount++;
            }
            if (balls[i] == '1') {
                rightCount--;
            }
    		// important: 状态转移方程，如下：
            dp[i] = dp[i-1] + leftCount - rightCount + balls[i-1] - balls[i];
        }
        return dp;
    }
```

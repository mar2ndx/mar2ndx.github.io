---
title: 739. Daily Temperatures
category: Leetcode
tags: []
comments: true
date: 2022-11-09 18:36
---



Link: https://leetcode.cn/problems/daily-temperatures/

# Question

difficulty: mid
adj diff: 2

    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:

    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Example 2:

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Example 3:

    Input: temperatures = [30,60,90]
    Output: [1,1,0]
    Constraints:

    	1 <= temperatures.length <= 105
    	30 <= temperatures[i] <= 100

# Code

```
    public int[] dailyTemperatures(int[] temperatures) {
        int len = temperatures.length;
        int[] ans = new int[len];
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = len - 1; i >= 0; i--) {
            while (!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? 0 : stack.peek() - i;
            stack.push(i);
        }
        return ans;
    }
```

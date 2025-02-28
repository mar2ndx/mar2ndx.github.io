---
title: 983. Minimum Cost For Tickets
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---


Link: https://leetcode.cn/problems/minimum-cost-for-tickets/

# Question

difficulty: mid
adj diff: 4

    You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

    Train tickets are sold in three different ways:

    	a 1-day pass is sold for costs[0] dollars,
    	a 7-day pass is sold for costs[1] dollars, and
    	a 30-day pass is sold for costs[2] dollars.

    The passes allow that many days of consecutive travel.

    	For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.

    Example 1:

    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
    On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
    On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
    In total, you spent $11 and covered all the days of your travel.

    Example 2:

    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
    On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
    In total, you spent $17 and covered all the days of your travel.

    Constraints:

    	1 <= days.length <= 365
    	1 <= days[i] <= 365
    	days is in strictly increasing order.
    	costs.length == 3
    	1 <= costs[i] <= 1000

这道题的难点在于：动态规划不是从 1 到 n 这么简单，而是通过 days array 跳着来。

中间跳过的天数，一律 fill with 之前的值。eg. dp[] = {0, 2, 2, 2, 4, 4, 4, 4, 12, 12, 12, 12, 12, 12....}

# Code

```
    public int mincostTickets(int[] days, int[] costs) {
        int len = days.length;
        int duration = days[len - 1];
        int[] dp = new int[duration + 1];

        for (int i = 0; i < len; i++) {
            // need to trave on day indexed at days[i]
            int cur = days[i];
            // dp[i] represents the cost till day i
            // if need to travel day i, then check price, otherwise = last
            // eg. dp[] = {0, 2, 2, 2, 4....}
            dp[cur] = dp[cur - 1] + costs[0];
            int pass7 = (cur - 7) <= 0 ? costs[1] : costs[1] + dp[cur - 7];
            int pass30 = (cur - 30) <= 0 ? costs[2] : costs[2] + dp[cur - 30];
            dp[cur] = Math.min(dp[cur], Math.min(pass30, pass7));
            if (i != len - 1) {
                for (int j = days[i] + 1; j < days[i + 1]; j++) {
                    dp[j] = dp[j - 1];
                }
            }
        }
        return dp[duration];
    }
```

---
title: 875. Koko Eating Bananas
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/koko-eating-bananas/

# Question

difficulty: mid
adj diff: 4

    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

    Example 1:

    Input: piles = [3,6,7,11], h = 8
    Output: 4

    Example 2:

    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

    Example 3:

    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

    Constraints:

    	1 <= piles.length <= 104
    	piles.length <= h <= 109
    	1 <= piles[i] <= 109

koko 吃香蕉，比较经典又特殊的一类 二分搜索 问题。

# Code

```
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int len = piles.length;
        if (h < len) return -1;
        int minSpeed = Integer.MAX_VALUE;
        int min = 1;
        int max = piles[len - 1];
        while (min < max) {
            int speed = min + (max - min) / 2;
            int hours = 0;
            // eat mid number per hours, from len piles
            for (Integer i: piles) {
                hours += (i - 1) / speed + 1;
            }
            if (hours <= h) {
                // finish earning within h time, next time eat slower
                minSpeed = Math.min(minSpeed, speed);
                max = speed;
            } else {
                // need to eat more
                min = speed + 1;
            }
        }
        return minSpeed == Integer.MAX_VALUE ? piles[len - 1] : minSpeed;
    }
```

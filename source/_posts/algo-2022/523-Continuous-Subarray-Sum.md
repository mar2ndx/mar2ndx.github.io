---
title: 523. Continuous Subarray Sum
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---


Link: https://leetcode.cn/problems/continuous-subarray-sum/

# Question

difficulty: mid
adj diff: 2

    Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

    Example 1:

    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
    Example 2:

    Input: nums = [23,2,6,4,7], k = 6
    Output: true
    Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
    42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
    Example 3:

    Input: nums = [23,2,6,4,7], k = 13
    Output: false

    Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 109
    0 <= sum(nums[i]) <= 231 - 1
    1 <= k <= 231 - 1

就是用一个 map 不断的记录就行了。

# Code

```
    public boolean checkSubarraySum(int[] nums, int k) {
        int len = nums.length;
        int[] prefixSum = new int[len + 1];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);

        for (int i = 1; i <= len; i++) {
            prefixSum[i] = (prefixSum[i - 1] + nums[i - 1]) % k;
            if (map.containsKey(prefixSum[i])) {
                if (i - map.get(prefixSum[i]) > 2)
                // check the subarray length (need to be at least 2)
                    return true;
            } else {
                map.put(prefixSum[i], i - 1);
            }
        }
        return false;
    }
```

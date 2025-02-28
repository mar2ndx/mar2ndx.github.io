---
title: 719. Find K-th Smallest Pair Distance
category: Leetcode
tags: []
comments: true
date: 2022-11-09 18:44
---



Link: https://leetcode.cn/problems/find-k-th-smallest-pair-distance/

# Question

difficulty: hard
adj diff: 5

    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

    Example 1:

    Input: nums = [1,3,1], k = 1
    Output: 0

    Explanation: Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.

    Example 2:

    Input: nums = [1,1,1], k = 2
    Output: 0

    Example 3:

    Input: nums = [1,6,1], k = 3
    Output: 5
     
    Constraints:

    n == nums.length
    2 <= n <= 104
    0 <= nums[i] <= 106
    1 <= k <= n * (n - 1) / 2

一道比较经典的**二分搜索**问题。

基本思路：选择一个 number，数一下有多少个 pair difference 比这个 number 小。

1. 如果 < k 个，那就选一个更大的 number。
1. 否则 >= k 个，则选更小的 number。

（注意：count pair 的子方法，无需二分搜索，直接**双指针**一次遍历就行了）

# Code

代码还是挺难的。

```
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int len = nums.length;
        int small = 0;
        int large = nums[len - 1] - nums[0];

        while (small < large) {
            int mid = small + large >> 1; // specila careful here!
            if (smallerPairs(nums, len, mid) < k) {
                small = mid + 1;
            } else {
                large = mid;
            }
        }
        return small;
    }

    private int smallerPairs(int[] nums, int len, int target) {
        // return how many pairs have distance <= target
        // eg [1, 1, 3] target = 0 return 1;
        // eg [1, 1, 3] target = 2 return 3;
        int count = 0;
        int right = 1;
        for (int i = 0; i < len - 1; i++) {
            while (right < len && nums[right] - nums[i] <= target) {
                right++;
            }
            count += right - i - 1;
        }
        return count;
    }
}
```

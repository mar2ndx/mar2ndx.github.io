---
title: 1567. Maximum Length of Subarray With Positive Product
category: Leetcode
tags: []
comments: true
date: 2022-11-08 23:21
---


Link: https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/

# Question

difficulty: mid
adj diff:

    Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

    A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

    Return the maximum length of a subarray with positive product.

     

    Example 1:

    Input: nums = [1,-2,-3,4]
    Output: 4
    Explanation: The array nums already has a positive product of 24.
    Example 2:

    Input: nums = [0,1,-2,-3,-4]
    Output: 3
    Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
    Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
    Example 3:

    Input: nums = [-1,-2,-3,0,1]
    Output: 2
    Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
     

    Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

重点：正数不用管，负数 count 一下。

# Code

```
class Solution {
    public int getMaxLen(int[] nums) {
        int len = nums.length;
        int firstPos = -1; // careful here!!!
        int firstNeg = -1;
        int countNeg = 0;
        int maxLen = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] == 0) {
                firstPos = i; // careful here!!!
                firstNeg = -1;
                countNeg = 0;
            } else if (nums[i] < 0) {
                countNeg++;
                if (firstNeg == -1) {
                    firstNeg = i;
                }
            }

            // check length (product is positive)
            if (countNeg % 2 == 1) {
                // odd number of '-', thus need to remove a negative
                maxLen = Math.max(maxLen, i - firstNeg);
            } else {
                maxLen = Math.max(maxLen, i - firstPos);
            }
        }
        return maxLen;
    }
}
```

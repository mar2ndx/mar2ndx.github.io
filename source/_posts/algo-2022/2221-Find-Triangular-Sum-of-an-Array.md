---
title: 2221. Find Triangular Sum of an Array
category: Leetcode
tags: []
comments: true
date: 2022-11-08 23:12
---


Link: https://leetcode.cn/problems/find-triangular-sum-of-an-array/

# Question

difficulty: mid
adj diff: 3

    You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

    The triangular sum of nums is the value of the only element present in nums after the following process terminates:

    Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
    For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
    Replace the array nums with newNums.
    Repeat the entire process starting from step 1.
    Return the triangular sum of nums.

     

    Example 1:


    Input: nums = [1,2,3,4,5]
    Output: 8
    Explanation:
    The above diagram depicts the process from which we obtain the triangular sum of the array.
    Example 2:

    Input: nums = [5]
    Output: 5
    Explanation:
    Since there is only one element in nums, the triangular sum is the value of that element itself.
     

    Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 9

并没有什么牛逼的数学算法。

直接实现就行！

（我曾经尝试着一个牛逼的 mathematical 算法，结果失败了。。。代码如下）

    class Solution {
        public int triangularSum(int[] nums) {
            // for 1 levels: 1*nums[0]
            // for 2 levels: 1*nums[0] + 1*nums[1]
            // for 3 levels: 1*nums[0] + 2*nums[1] + 1*nums[2]
            // for 4 levels: 1*nums[0] + 3*nums[1] + 3*nums[2] + 1*nums[3]
            // for 5 levels: 1*nums[0] + 4*nums[1] + 6*nums[2] + 4*nums[3] + 1*nums[4]
            // for 6 levels: 1*nums[0] + 5*nums[1] + 10*nums[2] + 10*nums[3] + 5*nums[4] + 1*nums[5]
            // if i = level
            int len = nums.length;
            long[] times = new long[len];
            times[0] = 1;
            for (int i = 1; i < len; i++) {
                for (int j = i; j >= 1; j--) {
                    times[j] = times[j - 1] + times[j];
                }
            }

            long sum = 0;
            for (int i = 0; i < len; i++) {
                sum += (long) nums[i] * times[i];
                sum %= 10l;
            }
            return (int) sum;
        }
    }

以上代码 170 / 300 个通过测试用例。

# Code

直接 - 杨辉三角变式。

```
class Solution {
    public int triangularSum(int[] nums) {
        int len = nums.length;
        for (int i = len - 1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                nums[j] = (nums[j + 1] + nums[j]) % 10;
            }
        }
        return nums[0];
    }
}
```

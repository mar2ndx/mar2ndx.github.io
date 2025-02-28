---
title: 1712. Ways to Split Array Into Three Subarrays
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/

# Question

difficulty: mid
adj diff: 4

    A split of an integer array is good if:

    	The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
    	The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.

    Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [1,1,1]
    Output: 1
    Explanation: The only good way to split nums is [1] [1] [1].

    Example 2:

    Input: nums = [1,2,2,2,5,0]
    Output: 3
    Explanation: There are three good ways of splitting nums:
    [1] [2] [2,2,5,0]
    [1] [2,2] [2,5,0]
    [1,2] [2,2] [5,0]

    Example 3:

    Input: nums = [3,2,1]
    Output: 0
    Explanation: There is no good way to split nums.

    Constraints:

    	3 <= nums.length <= 105
    	0 <= nums[i] <= 104

这个题是二分搜索。

我没写出来。

# Code

以下的代码 work：78 / 88 个通过测试用例

But：超出时间限制

```
    public int waysToSplit(int[] nums) {
        int n = nums.length;
        long[] sum = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        // special case: all 0s
        if (sum[n] == 0) {
            return (n - 1)/2 * n;
        }

        // pick a k, j as the start point of range2 and range3
        // 优化：k依然像这样穷举，但是j可以二分搜索（不过要搜2次）。
        // 第一次，搜j的最小可能值；第二次，搜j的最大可能值。就不写代码了。
        int count = 0;
        for (int k = 1; k < n; k++) {
            if (sum[k] > sum[n] / 3) {
                break;
            }
            for (int j = k + 1; j < n; j++) {
                // the 3 ranges are: [0, k - 1],
                // [k, j - 1], and [j, n - 1]
                if (sum[k] > sum[j] - sum[k]) {
                    continue;
                } else if (sum[j] - sum[k] > sum[n] - sum[j]) {
                    break;
                }
                count++;
            }
        }
        return count;
    }
```

以下是别人的代码，2 次二分搜索，work：

```
    public int waysToSplit(int[] nums) {
        final int MODULO = 1000000007;
        int ways = 0;
        int n = nums.length;
        int[] prefixSums = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSums[i + 1] = prefixSums[i] + nums[i];
        }
        int total = prefixSums[n];
        int leftMax = total / 3;
        for (int i = 1; i <= n - 2 && prefixSums[i] <= leftMax; i++) {
            int midMin = prefixSums[i] * 2, midMax = prefixSums[i] + (total - prefixSums[i]) / 2;
            int start = searchStart(prefixSums, midMin, i + 1, n);
            int end = searchEnd(prefixSums, midMax, i, n - 1);
            ways = (ways + (end - start + 1)) % MODULO;
        }
        return ways;
    }

    public int searchStart(int[] prefixSums, int target, int low, int high) {
        while (low < high) {
            int tmp = low + (high - low) / 2;
            if (prefixSums[tmp] >= target) {
                high = tmp;
            } else {
                low = tmp + 1;
            }
        }
        return low;
    }

    public int searchEnd(int[] prefixSums, int target, int low, int high) {
        while (low < high) {
            int tmp = low + (high - low + 1) / 2;
            if (prefixSums[tmp] <= target) {
                low = tmp;
            } else {
                high = tmp - 1;
            }
        }
        return low;
    }
```

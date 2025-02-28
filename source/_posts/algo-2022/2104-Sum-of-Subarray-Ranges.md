---
title: 2104. Sum of Subarray Ranges
category: Leetcode
tags: []
comments: true
date: 2022-11-09 19:12
---



Link: https://leetcode.cn/problems/sum-of-subarray-ranges/

# Question

difficulty: mid
adj diff: 5

    You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

    Return the sum of all subarray ranges of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:

    Input: nums = [1,2,3]
    Output: 4

    Explanation: The 6 subarrays of nums are the following:

        [1], range = largest - smallest = 1 - 1 = 0
        [2], range = 2 - 2 = 0
        [3], range = 3 - 3 = 0
        [1,2], range = 2 - 1 = 1
        [2,3], range = 3 - 2 = 1
        [1,2,3], range = 3 - 1 = 2

    So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

    Example 2:

    Input: nums = [1,3,3]
    Output: 4

    Explanation: The 6 subarrays of nums are the following:

        [1], range = largest - smallest = 1 - 1 = 0
        [3], range = 3 - 3 = 0
        [3], range = 3 - 3 = 0
        [1,3], range = 3 - 1 = 2
        [3,3], range = 3 - 3 = 0
        [1,3,3], range = 3 - 1 = 2

    So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

    Example 3:

    Input: nums = [4,-2,-3,4,1]
    Output: 59

    Explanation: The sum of all subarray ranges of nums is 59.
     

    Constraints:

    1 <= nums.length <= 1000
    -109 <= nums[i] <= 109
     
    Follow-up: Could you find a solution with O(n) time complexity?

这道题根本就不是 mid，而是 非常非常 hard！

这道题本质上是：

1. 先用**单调栈**记录一下最大，最小的边界。
1. 然后，我们就知道，一个数字 nums[i] 在这个边界之内，做了多少次 min value，做了多少次 max value。
1. Total count = Sum(所有的区间最大值) - Sum(所有的区间最小值)

看下面例子就懂了。

    eg. nums = {1 2 3 2},
    For nums[2] = 3:

    1.  Small boundaries are: (1, 3)
    1.  Large boundary is (-1, 4)

    Thus:

    1.  Total # of subarray that count nums[2] as smallest:
        1 x 1 = 1
    1.  Total # of subarray that count nums[2] as largest:
        3 x 2 = 6

最后，难点在于代码。

# Code

需要 2 个 stack，扫 2 遍。

1. 从左到右的时候，需要 count 所有的 duplicate elements
1. 从右往左的时候，skip 掉 duplicates，避免重复。

例如：{2, 2, 2}

对于中间那个数字，边界就是：(-1, 2) 而不是 (-1, 3)

另外，stack 的逻辑不能复用，所以代码比较长。

```
class Solution {
    public long subArrayRanges(int[] nums) {
        Stack<Integer> upStack = new Stack<Integer>();
        Stack<Integer> downStack = new Stack<Integer>();

        int len = nums.length;
        int[] usedAsLargestLeftBound = new int[len];
        int[] usedAsSmallestLeftBound = new int[len];

        // left --> right scan
        // (REMEMBER: count all duplicates)
        for (int i = 0; i < len; i++) {
            while (!upStack.isEmpty() && nums[upStack.peek()] > nums[i]) {
                upStack.pop();
            }
            // upStack is strictly increasing (no duplicates)
            usedAsSmallestLeftBound[i] = upStack.isEmpty() ? -1 : upStack.peek();
            upStack.push(i);

            while (!downStack.isEmpty() && nums[downStack.peek()] < nums[i]) {
                downStack.pop();
            }
            // downStack is strictly decreasing (no duplicates)
            usedAsLargestLeftBound[i] = downStack.isEmpty() ? -1 : downStack.peek();
            downStack.push(i);
        }

        // right --> left scan
        // (REMEMBER: DO NOT count ANY duplicate)
        int[] usedAsLargestRightBound = new int[len];
        int[] usedAsSmallestRightBound = new int[len];
        upStack.clear();
        downStack.clear();

        for (int w = len - 1; w >= 0; w--) {
            while (!upStack.isEmpty() && nums[upStack.peek()] >= nums[w]) {
                upStack.pop();
            }
            // upStack is increasing (with duplicates in stack)
            usedAsSmallestRightBound[w] = upStack.isEmpty() ? len : upStack.peek();
            upStack.push(w);

            while (!downStack.isEmpty() && nums[downStack.peek()] <= nums[w]) {
                downStack.pop();
            }
            // downStack is decreasing (with duplicates in stack)
            usedAsLargestRightBound[w] = downStack.isEmpty() ? len : downStack.peek();
            downStack.push(w);
        }

        long sum = 0;
        for (int i = 0; i < len; i++) {
            sum += (long) nums[i] * (usedAsLargestRightBound[i] - i) * (i - usedAsLargestLeftBound[i]);
            sum -= (long) nums[i] * (usedAsSmallestRightBound[i] - i) * (i - usedAsSmallestLeftBound[i]);
        }
        return sum;
    }
}
```

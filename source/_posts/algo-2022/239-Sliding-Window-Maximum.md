---
title: 239. Sliding Window Maximum
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---



Link: https://leetcode.cn/problems/sliding-window-maximum/

# Question

difficulty: high
adj diff: 4

    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.

    Example 1:

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Example 2:

    Input: nums = [1], k = 1
    Output: [1]

    Constraints:

    	1 <= nums.length <= 105
    	-104 <= nums[i] <= 104
    	1 <= k <= nums.length

这道题，只要好好写，注意边界就可以了。

单调递减队列问题。

注意的就是 = 的情况。相等的元素，保留在 list 中，一个一个地 remove，没问题。

# Code

```
    public int[] maxSlidingWindow(int[] nums, int k) {
        int len = nums.length;
        int[] ans = new int[len + 1 - k];
        List<Integer> list = new LinkedList<Integer>();

        // init the windows of size k elements
        for (int i = 0; i < k; i++) {
            while (list.size() > 0 && list.get(list.size() - 1) < nums[i]) {
                list.remove(list.size() - 1);
            }
            list.add(nums[i]);
        }

        for (int i = k; i < len; i++) {
            ans[i - k] = list.get(0);
            // remove nums[i-k+1], add nums[i]
            if (list.get(0) == nums[i - k]) {
                list.remove(0);
            }
            while (list.size() > 0 && list.get(list.size() - 1) < nums[i]) {
                list.remove(list.size() - 1);
            }
            list.add(nums[i]);
        }
        ans[len - k] = list.get(0);
        return ans;
    }
```

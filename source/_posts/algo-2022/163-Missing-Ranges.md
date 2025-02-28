---
title: 163. Missing Ranges
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/missing-ranges/

# Question

difficulty: easy
adj diff: 2

    You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

    A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

    Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

    Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

    Example 1:

    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: ["2","4->49","51->74","76->99"]
    Explanation: The ranges are:
    [2,2] --> "2"
    [4,49] --> "4->49"
    [51,74] --> "51->74"
    [76,99] --> "76->99"
    Example 2:

    Input: nums = [-1], lower = -1, upper = -1
    Output: []
    Explanation: There are no missing ranges since there are no missing numbers.

    Constraints:

    -109 <= lower <= upper <= 109
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    All the values of nums are unique.

注意：lower 和 upper 都在 range 之外，不在之内。

单纯的代码实现问题。

# Code

```
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> ans = new ArrayList<>();
        int len = nums.length;
        if (len == 0) {
            ans.add(helper(lower - 1, upper + 1));
            return ans;
        }

    	// first range
        if (lower < nums[0]) {
    		ans.add(helper(lower - 1, nums[0]));
    	}

    	// middle ranges
        for (int i = 0; i < len - 1; i++) {
            if (nums[i+1] - nums[i] == 1) {
    			continue;
    		} else {
    			ans.add(helper(nums[i], nums[i + 1]));
    		}
        }

    	// last range
        if (upper > nums[len - 1]) {
    		ans.add(helper(nums[len - 1], upper + 1));
    	}

        return ans;
    }

    private String helper(int left, int right) {
        StringBuilder builder = new StringBuilder();
        if (left + 2 == right) {
    		builder.append(left + 1);
    	} else {
    		builder.append(left + 1).append("->").append(right - 1);
    	}
        return builder.toString();
    }
```

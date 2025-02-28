---
title: 340. Longest Substring with At Most K Distinct Characters
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/

# Question

difficulty: mid
adj diff: 4

    Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

    Example 1:

    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.
    Example 2:

    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.

    Constraints:

    1 <= s.length <= 5 * 104
    0 <= k <= 50

# Code

```
    class Solution {
    	public int lengthOfLongestSubstringKDistinct(String s, int k) {
    		int len = s.length();
    		int distinctLetters = 0;
    		int maxLength = 0;
    		int left = 0;
    		int right = 0;
    		int[] map = new int[128];

    		while (right < len) {
    			if (distinctLetters <= k) {
    				maxLength = Math.max(maxLength, right - left);
    				char nextChar = s.charAt(right++);
    				if (map[nextChar] == 0) {
    					distinctLetters++;
    				}
    				map[nextChar]++;
    			} else {
    				// move left till distinctLetters == k
    				while (distinctLetters > k) {
    					char nextChar = s.charAt(left++);
    					if (map[nextChar] == 1) {
    						distinctLetters--;
    					}
    					map[nextChar]--;
    				}
    			}
    		}
    		if (distinctLetters <= k) {
    			maxLength = Math.max(maxLength, right - left);
    		}
    		return maxLength;
    	}
    }
```

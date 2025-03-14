---
title: 696. Count Binary Substrings
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---



Link: https://leetcode.cn/problems/count-binary-substrings/

# Question

difficulty: easy
adj diff: 4

难题，我根本就不会做。看答案勉强看会了。

    Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they occur.

    Example 1:

    Input: s = "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    Example 2:

    Input: s = "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

    Constraints:

    	1 <= s.length <= 105
    	s[i] is either '0' or '1'.

# Code

```
    public int countBinarySubstrings(String s) {
        int len = s.length();
        List<Integer> list = new ArrayList<Integer>();

        // build the list
        int p = 0;
        char ch = s.charAt(0);
        int count = 0;
        while (p < len) {
            while (p < len && s.charAt(p) == ch) {
                p++;
                count++;
            }
            if (p < len) ch = s.charAt(p);
            list.add(count);
            count = 0;
        }

        // traverse the list
        int total = 0;
        for (int i = 1; i < list.size(); i++) {
            total += Math.min(list.get(i - 1), list.get(i));
        }
        return total;
    }
```

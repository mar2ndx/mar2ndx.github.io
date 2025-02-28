---
title: 1864. Minimum Number of Swaps to Make the Binary String Alternating
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

# Question

difficulty: mid
adj diff: 4

    Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

    The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

    Any two characters may be swapped, even if they are not adjacent.

    Example 1:

    Input: s = "111000"
    Output: 1
    Explanation: Swap positions 1 and 4: "111000" -> "101010"
    The string is now alternating.

    Example 2:

    Input: s = "010"
    Output: 0
    Explanation: The string is already alternating, no swaps are needed.

    Example 3:

    Input: s = "1110"
    Output: -1

    Constraints:

    	1 <= s.length <= 1000
    	s[i] is either '0' or '1'.

borning question.

# Code

```
    public int minSwaps(String s) {

        // 类似前缀和
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                count++;
            }
            else {
                count--;
            }
        }

        // 如果01差值大于1自然无法构建，那么就是-1
        if (Math.abs(count) > 1) {
            return -1;
        }

        // 0、1一样多，那么就两种情况取小值
        if (count == 0) {
            int count1 = 0;
            int count2 = 0;
            for (int i = 0; i < s.length(); i++) {
                if (i % 2 == 0 && s.charAt(i) == '0') {
                    count1++;
                }
                if (i % 2 == 1 && s.charAt(i) == '0') {
                    count2++;
                }
            }
            return Math.min(count1, count2);
        }

        // 1 更多
        if (count == 1) {
            int count1 = 0;
            for (int i = 0; i < s.length(); i++) {
                if (i % 2 == 0 && s.charAt(i) == '0') {
                    count1++;
                }
            }
            return count1;
        }

        // 0 更多
        int count1 = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && s.charAt(i) == '1') {
                count1++;
            }
        }
        return count1;
    }
```

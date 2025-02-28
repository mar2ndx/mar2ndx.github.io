---
title: 1249. Minimum Remove to Make Valid Parentheses
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/

# Question

difficulty: mid
adj diff: 3

    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    	It is the empty string, contains only lowercase characters, or
    	It can be written as AB (A concatenated with B), where A and B are valid strings, or
    	It can be written as (A), where A is a valid string.

    Example 1:

    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    Example 2:

    Input: s = "a)b(c)d"
    Output: "ab(c)d"

    Example 3:

    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

    Constraints:

    	1 <= s.length <= 105
    	s[i] is either'(' , ')', or lowercase English letter.

# Code

```
    public String minRemoveToMakeValid(String s) {
        int p = 0;
        Stack<Integer> stack = new Stack<Integer>();
        int leftParenthisCount = 0;
        while (p < s.length()) {
            if (stack.isEmpty() && s.charAt(p) == ')') {
                s = s.substring(0, p) + s.substring(p + 1);
                continue; // remove a ')' and keep p un-moved
            } else if (s.charAt(p) == '(') {
                stack.push(p);
                leftParenthisCount++;
            } else if (s.charAt(p) == ')') {
                if (leftParenthisCount > 0) {
                    leftParenthisCount--;
                } else {
                    s = s.substring(0, p) + s.substring(p + 1);
                    continue; // remove a ')' and keep p un-moved
                }
            }
            p++;
        }
        for (int i = 0; i < leftParenthisCount; i++) {
            p = stack.pop();
            s = s.substring(0, p) + s.substring(p + 1);
        }
        return s;
    }
```

---
title: 394. Decode String
category: Leetcode
tags: []
comments: true
date: 2022-11-15 00:48
---



Link: https://leetcode.cn/problems/decode-string/

# Question

difficulty: mid
adj diff: 3

    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

    The test cases are generated so that the length of the output will never exceed 105.
    Example 1:

    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example 2:

    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    Constraints:

    	1 <= s.length <= 30
    	s consists of lowercase English letters, digits, and square brackets '[]'.
    	s is guaranteed to be a valid input.
    	All the integers in s are in the range [1, 300].

用 Stack 来做。

# Code

```
    public String decodeString(String s) {
        int len = s.length();
        Stack<Character> stack = new Stack<Character>();
        for (int k = 0; k < len; k++) {
            char c = s.charAt(k);
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                List<Character> list = new ArrayList<Character>();
                while (stack.peek() != '[') {
                    list.add(stack.pop());
                }
                stack.pop();
                int times = 0;
                int zeros = 1;
                while (!stack.isEmpty() && (stack.peek() >= '0' && stack.peek() <= '9')) {
                    times += zeros * (int) (stack.pop() - '0');
                    zeros *= 10;
                }
                for (int i = 0; i < times; i++) {
                    for (int j = list.size() - 1; j >= 0; j--) {
                        stack.push(list.get(j));
                    }
                }
            } else { // either number or char
                stack.push(c);
            }
        }
        String res = "";
        while (!stack.isEmpty()) {
            res = stack.pop() + res;
        }
        return res;
    }
```

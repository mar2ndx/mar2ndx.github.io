---
title: 1405. Longest Happy String
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/longest-happy-string/

# Question

difficulty: mid
adj diff: 4

    A string s is called happy if it satisfies the following conditions:

    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.
    Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

    A substring is a contiguous sequence of characters within a string.
    Example 1:

    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
    Example 2:

    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.

    Constraints:

    0 <= a, b, c <= 100
    a + b + c > 0

# Code

```
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder sb = new StringBuilder();
        Pair[] pairs = {
            new Pair('a', a),
            new Pair('b', b),
            new Pair('c', c)
        };

        Arrays.sort(pairs);
        build(sb, 'z', pairs);
        return sb.toString();
    }

    private void build(StringBuilder sb, char preChar, Pair[] pairs) {
        int nextIndex = -1;
        String str = sb.toString();
        int len = str.length();

        if (len < 2 || preChar != pairs[0].abc) {
            nextIndex = 0;
        } else if (str.charAt(len - 2) == str.charAt(len - 1)) {
            nextIndex = 1;
        } else {
            nextIndex = 0;
        }

        if (pairs[nextIndex].count == 0) {
            return;
        }

        char nextChar = pairs[nextIndex].abc;
        sb.append(nextChar);
        pairs[nextIndex].count = pairs[nextIndex].count - 1;
        Arrays.sort(pairs);
        build(sb, nextChar, pairs);
    }

    class Pair implements Comparable<Pair>{
        char abc;
        int count;

        public Pair(char x, int y) {
            abc = x;
            count = y;
        }

        public int compareTo(Pair p) {
            return p.count - this.count;
        }
    }
```

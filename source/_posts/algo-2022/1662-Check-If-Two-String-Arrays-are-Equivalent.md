---
title: 1662. Check If Two String Arrays are Equivalent
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:41
---



Link: https://leetcode.cn/problems/check-if-two-string-arrays-are-equivalent/

# Question

difficulty: easy
adj diff: 2

    Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated in order forms the string.

    Example 1:

    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
    word1 represents string "ab" + "c" -> "abc"
    word2 represents string "a" + "bc" -> "abc"
    The strings are the same, so return true.

    Example 2:

    Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
    Output: false

    Example 3:

    Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
    Output: true

    Constraints:

    	1 <= word1.length, word2.length <= 103
    	1 <= word1[i].length, word2[i].length <= 103
    	1 <= sum(word1[i].length), sum(word2[i].length) <= 103
    	word1[i] and word2[i] consist of lowercase letters.

# Code

```
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int len1 = word1.length;
        int len2 = word2.length;
        int[] indexes = new int[4];

        while (indexes[0] < len1 && indexes[2] < len2) {
            // check same char (or not)
            if (word1[indexes[0]].charAt(indexes[1]) != word2[indexes[2]].charAt(indexes[3])) {
                return false;
            }
            indexes[1]++;
            indexes[3]++;

            // fix indexes, point to valid char
            if (indexes[1] == word1[indexes[0]].length()) {
                indexes[0]++;
                indexes[1] = 0;
            }
            if (indexes[3] == word2[indexes[2]].length()) {
                indexes[2]++;
                indexes[3] = 0;
            }
        }
        return (indexes[0] == len1 && indexes[2] == len2);
    }
```

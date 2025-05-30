---
title: 1153. String Transforms Into Another String
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/string-transforms-into-another-string/

# Question

difficulty: high
adj diff: 3

    Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

    In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

    Return true if and only if you can transform str1 into str2.

    Example 1:

    Input: str1 = "aabcc", str2 = "ccdee"
    Output: true
    Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
    Example 2:

    Input: str1 = "leetcode", str2 = "codeleet"
    Output: false
    Explanation: There is no way to transform str1 to str2.

    Constraints:

    1 <= str1.length == str2.length <= 104
    str1 and str2 contain only lowercase English letters.

# Code

```
    public boolean canConvert(String str1, String str2) {
        int len = str1.length();
        if (len != str2.length()) return false;
        if (str2.equals(str1)) return true;

        Map<Character, Character> map = new HashMap<Character, Character>();
        Set<Character> set=new HashSet<>();

        for (int i = 0; i < len; i++) {
            char c1 = str1.charAt(i);
            char c2 = str2.charAt(i);

            // first, check s1 -> s2 letter mapping are correct, no distored positions.
            if (map.containsKey(c1)) {
                if (map.get(c1) != c2) {
                    return false;
                }
            } else {
                map.put(c1, c2);
            }
            // Very important: check s2, if all 26 letters apear or not!
            set.add(c2);
        }
        return set.size() < 26;
    }
```

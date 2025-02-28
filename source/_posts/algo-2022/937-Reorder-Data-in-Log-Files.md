---
title: 937. Reorder Data in Log Files
category: Leetcode
tags: []
comments: true
date: 2022-11-02 13:41
---


Link: https://leetcode.cn/problems/reorder-data-in-log-files/

# Question

difficulty: mid
adj diff: 3

	You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

	There are two types of logs:

		Letter-logs: All words (except the identifier) consist of lowercase English letters.
		Digit-logs: All words (except the identifier) consist of digits.

	Reorder these logs so that:

		The letter-logs come before all digit-logs.
		The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
		The digit-logs maintain their relative ordering.

	Return the final order of the logs.

	 

	Example 1:

	Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
	Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
	Explanation:
	The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
	The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

	Example 2:

	Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
	Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

	 

	Constraints:

		1 <= logs.length <= 100
		3 <= logs[i].length <= 100
		All the tokens of logs[i] are separated by a single space.
		logs[i] is guaranteed to have an identifier and at least one word after the identifier.

主要就是考察 comparator 怎么写.

# Code

```
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, new Comparator<String>() {
            public int compare(String a, String b) {
                String[] log1 = split(a);
                String[] log2 = split(b);
                char char1 = log1[1].charAt(0);
                char char2 = log2[1].charAt(0);
                if (isDigit(char1) && isDigit(char2)) {
                    return 0;
                } else if (isDigit(char1)) {
                    return 1;
                } else if (isDigit(char2)) {
                    return -1;
                } else if (log1[1].equals(log2[1])) {
                    return log1[0].compareTo(log2[0]);
                } else {
                    return log1[1].compareTo(log2[1]);
                }
            }
        });
        return logs;
    }

    private boolean isDigit(char ch) {
        return ('0' <= ch && ch <= '9');
    }

    private String[] split(String str) {
        String[] array = new String[2];
        int p = 0;
        while (p < str.length() && str.charAt(p) != ' ') {
            p++;
        }
        array[0] = str.substring(0, p);
        array[1] = str.substring(p + 1);
        return array;
    }
}
```

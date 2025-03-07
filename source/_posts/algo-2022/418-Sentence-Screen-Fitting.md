---
title: 418. Sentence Screen Fitting
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/sentence-screen-fitting/

# Question

difficulty: mid
adj diff: 5

    Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

    The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

    Example 1:

    Input: sentence = ["hello","world"], rows = 2, cols = 8
    Output: 1
    Explanation:
    hello---
    world---
    The character '-' signifies an empty space on the screen.
    Example 2:

    Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
    Output: 2
    Explanation:
    a-bcd-
    e-a---
    bcd-e-
    The character '-' signifies an empty space on the screen.
    Example 3:

    Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
    Output: 1
    Explanation:
    i-had
    apple
    pie-i
    had--
    The character '-' signifies an empty space on the screen.

    Constraints:

    1 <= sentence.length <= 100
    1 <= sentence[i].length <= 10
    sentence[i] consists of lowercase English letters.
    1 <= rows, cols <= 2 * 104

# Code

```
    class Solution {
    	public int wordsTyping(String[] sentence, int rows, int cols) {
    		int len = sentence.length;
    		int[] article = new int[len];
    		for (int i = 0; i < len; i++) {
    			article[i] = sentence[i].length();
    		}
    		int times = 0;

    		// One index to traverse the rows, another index to traverse the sentence
    		int rowIndex = 0;
    		int wordIndex = 0;
    		while (rowIndex < rows) {
    			int currentLen = 0;
    			while (currentLen + article[wordIndex] <= cols) {
    				currentLen += 1 + article[wordIndex++];
    				if (wordIndex == len) {
    					times++;
    					wordIndex = 0;
    				}
    			}
    			rowIndex++;
    		}
    		return times;
    	}
    }
```

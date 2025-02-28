---
title: "[NineChap 2.2] Sorted Array"
category: NineChap
tags: []
comments: true
date: 2014-06-09 00:00
---


## Sorted Array

#### Template

There is no template.

#### Question list

1. **[Remove Duplicates from Sorted Array](/leetcode/2014-05-09-Remove-Duplicates-from-Sorted-Array)**

2. **[Remove Duplicates from Sorted Array II](/leetcode/2014-05-22-Remove-Duplicates-from-Sorted-Array-II)**

3. **[Merge Sorted Array](/leetcode/2014-05-23-Merge-Sorted-Array)**

4. **[Median of Two Sorted Arrays](/leetcode/2014-04-26-Median-of-Two-Sorted-Arrays)**

5. **[Recover Rotated Sorted Array](/lintcode/2014-06-08-Recover-Rotated-Sorted-Array)**

#### Additional

1. **[Reverse Words in a String](/leetcode/2014-06-03-Reverse-Words-in-a-String)**

2. **Rotate String**

   Given string "abcdefg" and offset = 3, the rotated string is "efgabcd".

## Code

**Remove Duplicates from Sorted Array**

    public int removeDuplicates(int[] A) {
        if (A == null || A.length == 0) {
    		return 0;
    	}
    	int left = 1;
    	int right = 1;
    	while (right < A.length) {
    		if (A[right - 1] != A[right]) {
    			A[left] = A[right];
    			left++;
    		}
    		right++;
    	}
    	return left;
    }

**Remove Duplicates from Sorted Array II** - slightly difficult in coding

    public int removeDuplicates(int[] A) {
        if (A == null || A.length == 0) {
    		return 0;
    	}
    	int left = 1;
    	int right = 1;
    	boolean twice = false;
    	while (right < A.length) {
    		if (A[right - 1] != A[right]) {
    			A[left++] = A[right++];
    			twice = false;
    		} else if (!twice){
    			A[left++] = A[right++];
    			twice = true;
    		} else {
    			right++;
    		}
    	}
    	return left;
    }

**Merge Sorted Array**

Easy question, tail to head merge.

**Median of Two Sorted Arrays**

This question is Find kth largest from A&B. Refer to original post.

**Recover Rotated Sorted Array**

I wrote a new post.

**Reverse Words in a String**

    public String reverseWords(String s) {
    	if (s == null || s.length() == 0) {
    		return s;
    	}
    	String[] words = s.split(" ");
    	String firstReversed = "";
    	for (int i = 0; i < words.length; i ++) {
    	    if (words[i].equals("")) continue;
    		firstReversed += inPlaceReverse(words[i]) + " ";
    	}
    	return inPlaceReverse(firstReversed);
    }

    private String inPlaceReverse(String str) {
    	if (str == null || str.length() == 0) return str;
    	char[] chars = str.trim().toCharArray();
    	int left = 0;
    	int right = chars.length - 1;
    	while (left < right) {
    		char temp = chars[left];
    		chars[left] = chars[right];
    		chars[right] = temp;
    		left ++;
    		right --;
    	}
    	return String.valueOf(chars);
    }

**Rotate String**

Same strategy.

## Conclusion

1. If array is sorted, try binary search
2. If array is not sorted, try sort it first
3. When you see 'rotated array', think of 'list reverse'.

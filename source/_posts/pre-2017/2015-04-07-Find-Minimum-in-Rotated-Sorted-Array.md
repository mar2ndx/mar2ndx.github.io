---
title: "[LeetCode 153] Find Minimum in Rotated Sorted Array "
category: Leetcode
tags: []
comments: true
date: 2015-04-07 00:00
---


### Question 

[link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

<div class="question-content">
              <p></p><p>Suppose a sorted array is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., <code>0 1 2 4 5 6 7</code> might become <code>4 5 6 7 0 1 2</code>).</p>

<p>Find the minimum element.</p>

<p>You may assume no duplicate exists in the array.</p><p></p>
              
                <div id="tags" class="btn btn-xs btn-warning">Show Tags</div>
                <span class="hide">
                  
                  <a class="btn btn-xs btn-primary" href="/tag/array/">Array</a>
                  
                  <a class="btn btn-xs btn-primary" href="/tag/binary-search/">Binary Search</a>
                  
                </span>
              
            </div>

### Analysis

This question is very similar to __[LeetCode 33] Search in Rotated Sorted Array__. Note a few special cases. 

### Solution

Very good code can be found [here](http://www.programcreek.com/2014/02/leetcode-find-minimum-in-rotated-sorted-array/) and [here](http://www.sanfoundry.com/java-program-find-minimum-element-rotated-sorted-array-using-binary-search-approach/). 

### My Code

    public class Solution {
        public int findMin(int[] num) {
            if (num == null || num.length == 0) {
                return 0;
            }
            return helper(num, 0, num.length - 1);
        }

        private int helper(int[] num, int left, int right) {
            if (num[left] <= num[right]) {
                return num[left];
            } else if (left + 1 == right) {
                return num[right];
            }
            int mid = left + (right - left) / 2;
            if (num[mid] > num[left]) {
                return helper(num, mid, right);
            } else {
                return helper(num, left, mid);
            }
        }
    }

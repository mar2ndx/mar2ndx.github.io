---
title: "[LeetCode 108] Convert Sorted Array to Binary Search Tree"
category: Leetcode
tags: []
comments: true
date: 2014-05-26 00:00
---


### Question

[link](https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

<div class="question-content">
            <p></p><p>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.</p><p></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Frequency</td>
		<td bgcolor="yellow">3</td>
	</tr>
	<tr>
		<td>Difficulty</td>
		<td bgcolor="lime">2</td>
	</tr>
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="lime">2</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="yellow">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**My first understanding of this question is wrong**.

A BST does not necessarily have to fill in left side of the leaf as muc has possible. I was confusing "balanced binary tree" with "left-balanced binary tree".

> **A balanced binary tree** is commonly defined as a binary tree in which the depth of the left and right subtrees of every node differ by 1 or less

> **A left-balanced binary tree** is a balanced binary tree where the left sub-tree of each node is filled before the right sub-tree

### Solution

Then this question become straight-forward.

### Code

    public TreeNode sortedArrayToBST(int[] num) {
        if (num.length == 0) return null;
        return helper(num, 0, num.length - 1);
    }

    public TreeNode helper(int[] num, int start, int end) {
        if (start > end) return null;
        int mid = (start + end) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = helper(num, start, mid - 1);
        node.right = helper(num, mid + 1, end);
        return node;
    }

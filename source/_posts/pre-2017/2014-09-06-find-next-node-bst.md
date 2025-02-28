---
title: "[CC150v4] 4.5 Find Next Node in BST "
category: CC150v4
tags: []
comments: true
date: 2014-09-06 00:00
---


### Question

> Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.

### Solution

1. **If current node have a right child**, return the leftmost leaf of right child.

1. **If current node have no right child**:

   1. If current is parent's left child, then return parent node.

   1. If current is parent's right child, look all the way up until find a right-turning parent.

   1. If all parent is not right-turning. Return null.

### Code

**written by me**

    public static TreeNode inorderSucc(TreeNode e) {
    	if (e == null)
    		return null;
    	if (e.right != null) {
    		TreeNode p = e.right;
    		while (p.left != null) {
    			p = p.left;
    		}
    		return p;
    	} else {
    		TreeNode p = e.parent;
    		while (p != null && p.right == e) {
    			e = p;
    			p = e.parent;
    		}
    		return p;
    	}
    }

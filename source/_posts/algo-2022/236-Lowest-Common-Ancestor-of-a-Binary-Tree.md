---
title: 236. Lowest Common Ancestor of a Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

# Question

difficulty: mid
adj diff: 3

    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    Example 3:

    Input: root = [1,2], p = 1, q = 2
    Output: 1
    Constraints:

    	The number of nodes in the tree is in the range [2, 105].
    	-109 <= Node.val <= 109
    	All Node.val are unique.
    	p != q
    	p and q will exist in the tree.

# Code

```
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null)
            return null;
        if (root == p || root == q)
            return root;

        // depth-first search: find left and right
        TreeNode leftFound = lowestCommonAncestor(root.left, p, q);
        TreeNode rightFound = lowestCommonAncestor(root.right, p, q);

        if (leftFound == null) {
            return rightFound;
        } else if (rightFound == null) {
            return leftFound;
        } else {
            return root;
        }
    }
```

---
title: 993. Cousins in Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/cousins-in-binary-tree/

# Question

difficulty: easy
adj diff: 3

    Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

    Two nodes of a binary tree are cousins if they have the same depth with different parents.

    Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

    Example 1:

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

    Example 2:

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

    Example 3:

    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

    Constraints:

    	The number of nodes in the tree is in the range [2, 100].
    	1 <= Node.val <= 100
    	Each node has a unique value.
    	x != y
    	x and y are exist in the tree.

解法非常地类似 LCA 经典解法。

# Code

```
    public boolean isCousins(TreeNode root, int x, int y) {
        int res = depth(0, root, x, y);
        return res == Integer.MAX_VALUE;
    }

    private int depth(int level, TreeNode node, int x, int y) {
        if (node == null) {
            return -1;
        } else if (node.val == x || node.val == y) {
            return level;
        }

        int ll = depth(level + 1, node.left, x, y);
        int rr = depth(level + 1, node.right, x, y);
        if (ll == -1 && rr == -1) {
            return -1;
        } else if (ll == -1) {
            return rr;
        } else if (rr == -1) {
            return ll;
        } else {
            return ll == rr && ll - level > 1 ? Integer.MAX_VALUE : -1;
        }
    }
```

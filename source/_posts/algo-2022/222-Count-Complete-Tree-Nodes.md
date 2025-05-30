---
title: 222. Count Complete Tree Nodes
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/count-complete-tree-nodes/

# Question

difficulty: mid
adj diff: 3

    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.

    Example 1:

    Input: root = [1,2,3,4,5,6]
    Output: 6

    Example 2:

    Input: root = []
    Output: 0

    Example 3:

    Input: root = [1]
    Output: 1

    Constraints:

    	The number of nodes in the tree is in the range [0, 5 * 104].
    	0 <= Node.val <= 5 * 104
    	The tree is guaranteed to be complete.

判断左右 depth，是否相等。

# Code

```
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int depthLeft = depth(root.left);
        int depthRight = depth(root.right);
        if (depthLeft == depthRight) {
            // left tree is complete
            return (int) Math.pow(2, depthLeft) + countNodes(root.right);
        } else {
            return 1 + countNodes(root.left) + countNodes(root.right);
        }
    }

    private int depth(TreeNode node) {
        if (node == null) return 0;
        return depth(node.left) + 1;
    }
```

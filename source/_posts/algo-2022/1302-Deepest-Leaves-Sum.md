---
title: 1302. Deepest Leaves Sum
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/deepest-leaves-sum/

# Question

difficulty: mid
adj diff: 3

    Given the root of a binary tree, return the sum of values of its deepest leaves.
    Example 1:

    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

    Example 2:

    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 19
    Constraints:

    	The number of nodes in the tree is in the range [1, 104].
    	1 <= Node.val <= 100

# Code

```
    int sum;
    int maxLevel;

    public int deepestLeavesSum(TreeNode root) {
        dfs(root, 1);
        return sum;
    }

    private void dfs(TreeNode node, int level) {
        if (node == null) return;
        if (level > maxLevel) {
            maxLevel = level;
            sum = node.val;
        } else if (level == maxLevel) {
            sum += node.val;
        }
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    }
```

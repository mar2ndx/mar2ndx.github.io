---
title: 366. Find Leaves of Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---


Link: https://leetcode.cn/problems/find-leaves-of-binary-tree/

# Question

difficulty: mid
adj diff: 4

    Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

    Example 1:
    Input: root = [1,2,3,4,5]
    Output: [[4,5,3],[2],[1]]
    Explanation:
    [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
    Example 2:

    Input: root = [1]
    Output: [[1]]

    Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100

这个题不简单。主要是：从上往下扫的时候，先看到 root，后看到 leaf，这怎么 build 结果链条啊？

这个思路是：猜测这个 node 在 result list 的哪一层。我们暂且把这个 index 称为 leafLevel。

看代码吧，很短。

# Code

```
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        testDepth(ans, root);
        return ans;
    }

    private int testDepth(List<List<Integer>> ans, TreeNode node) {
        if (node == null) return 0;
        int leafLevel = 1 + Math.max(testDepth(ans, node.left), testDepth(ans, node.right));
        if (ans.size() < leafLevel) {
            // because the traverse always bottom-up, so it's safe to add to the end
            ans.add(new LinkedList<Integer>());
        }
        ans.get(leafLevel - 1).add(node.val);
        return leafLevel;
    }
}
```

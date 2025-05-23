---
title: 662. Maximum Width of Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-09 18:35
---



Link: https://leetcode.cn/problems/maximum-width-of-binary-tree/

# Question

difficulty: mid
adj diff: 3

    Given the root of a binary tree, return the maximum width of the given tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

    It is guaranteed that the answer will in the range of a 32-bit signed integer.

    Example 1:

    Input: root = [1,3,2,5,3,null,9]
    Output: 4

        Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

    Example 2:

    Input: root = [1,3,2,5,null,null,9,6,null,7]
    Output: 7

        Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

    Example 3:

    Input: root = [1,3,2,5]
    Output: 2

        Explanation: The maximum width exists in the second level with length 2 (3,2).

    Constraints:

    The number of nodes in the tree is in the range [1, 3000].
    -100 <= Node.val <= 100

DFS + 记忆搜索。

其实代码可以更简洁的。看下面。

# Code

Mine

```
    List<long[]> levelBoundaries = new LinkedList<long[]>();
    long maxWidth = 0;

    public int widthOfBinaryTree(TreeNode root) {
        dfs(root, 0, 0);
        return (int) maxWidth;
    }

    private void dfs(TreeNode node, int level, long index) {
        // for level = i, max # of nodes are: 2 ^ i
        if (node == null) return;
        if (levelBoundaries.size() <= level) {
            levelBoundaries.add(new long[]{index, index});
        }
        long[] boundary = levelBoundaries.get(level);
        boundary[0] = Math.min(boundary[0], index);
        boundary[1] = Math.max(boundary[1], index);

        maxWidth = Math.max(maxWidth, boundary[1] - boundary[0] + 1);

        dfs(node.left, level + 1, index * 2);
        dfs(node.right, level + 1, index * 2 + 1);
    }
```

Others

```
    class Solution {
        Map<Integer, Integer> levelMin = new HashMap<Integer, Integer>();

        public int widthOfBinaryTree(TreeNode root) {
            return dfs(root, 1, 1);
        }

        public int dfs(TreeNode node, int depth, int index) {
            if (node == null) {
                return 0;
            }
            levelMin.putIfAbsent(depth, index); // 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return Math.max(index - levelMin.get(depth) + 1, Math.max(dfs(node.left, depth + 1, index * 2), dfs(node.right, depth + 1, index * 2 + 1)));
        }
    }
```

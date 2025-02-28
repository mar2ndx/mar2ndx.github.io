---
title: 2096. Step-By-Step Directions From a Binary Tree Node to Another
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Question

difficulty: mid
adj diff: 4

    You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

    Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

    	'L' means to go from a node to its left child node.
    	'R' means to go from a node to its right child node.
    	'U' means to go from a node to its parent node.

    Return the step-by-step directions of the shortest path from node s to node t.

    Example 1:

    Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
    Output: "UURL"
    Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

    Example 2:

    Input: root = [2,1], startValue = 2, destValue = 1
    Output: "L"
    Explanation: The shortest path is: 2 → 1.
    Constraints:

    	The number of nodes in the tree is n.
    	2 <= n <= 105
    	1 <= Node.val <= n
    	All the values in the tree are unique.
    	1 <= startValue, destValue <= n
    	startValue != destValue

这道题，难点在于怎么 2 次找 path，写了好久，终于写完了。

很巧妙地用了复用了 printPath()方法。看代码。

# Code

```
    List<Character> finalPath = new LinkedList<Character>();

    public String getDirections(TreeNode root, int startValue, int destValue) {
        TreeNode lcaNode = lca(root, startValue, destValue);
        List<Character> tmpPath = new LinkedList<Character>();
        printPath(tmpPath, lcaNode, startValue, new char[]{'U', 'U'});
        printPath(tmpPath, lcaNode, destValue, new char[]{'L', 'R'});

        StringBuilder sb = new StringBuilder();
        for (Character c: finalPath) {
            sb.append(c);
        }
        return sb.toString();
    }

    private boolean printPath(List<Character> path, TreeNode current, int val, char[] chars) {
        if (current == null) {
            return false;
        } else if (current.val == val) {
            finalPath.addAll(path);
            return true;
        }

        path.add(chars[0]);
        boolean b = printPath(path, current.left, val, chars);
        path.remove(path.size() - 1);

        if (b == false) {
            path.add(chars[1]);
            b = printPath(path, current.right, val, chars);
            path.remove(path.size() - 1);
        }
        return b;
    }

    private TreeNode lca(TreeNode node, int p, int q) {
        if (node == null || node.val == p || node.val == q) {
            return node;
        }

        TreeNode ll = lca(node.left, p, q);
        TreeNode rr = lca(node.right, p, q);
        if (ll == null) {
            return rr;
        } else if (rr == null) {
            return ll;
        } else {
            return node;
        }
    }
```

---
title: 655. Print Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/print-binary-tree/solution/shu-chu-er-cha-shu-by-leetcode-solution-cnxu/

    Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

    	The height of the tree is height and the number of rows m should be equal to height + 1.
    	The number of columns n should be equal to 2height+1 - 1.
    	Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
    	For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
    	Continue this process until all the nodes in the tree have been placed.
    	Any empty cells should contain the empty string "".

    Return the constructed matrix res.
    Example 1:

    Input: root = [1,2]
    Output:
    [["","1",""],
     ["2","",""]]

    Example 2:

    Input: root = [1,2,3,null,4]
    Output:
    [["","","","1","","",""],
     ["","2","","","","3",""],
     ["","","4","","","",""]]
    Constraints:

    	The number of nodes in the tree is in the range [1, 210].
    	-99 <= Node.val <= 99
    	The depth of the tree will be in the range [1, 10].

纯 ArrayList 的实现，不难。

# Code

```
    public List<List<String>> printTree(TreeNode root) {
        int h = height(root);
        List<List<String>> ans = new ArrayList<List<String>>(h);
        for (int i = 0; i < h; i++) {
            List<String> tmp = new ArrayList<String>();
            for (int j = 0; j < Math.pow(2, h) - 1; j++) {
                tmp.add("");
            }
            ans.add(tmp);
        }
        dfs(ans, root, (int) Math.pow(2, h - 1) - 1, 0, h);
        return ans;
    }

    private void dfs(List<List<String>> ans, TreeNode node, int col, int row, int h) {
        if (node == null) return;
        List<String> printRow = ans.get(row);
        printRow.set(col, "" + node.val);
        if (h > row + 1) {
            dfs(ans, node.left, col - (int) Math.pow(2, h - row - 2), row + 1, h);
            dfs(ans, node.right, col + (int) Math.pow(2, h - row - 2), row + 1, h);
        }
    }

    private int height(TreeNode node) {
        if (node == null) return 0;
        return 1 + Math.max(height(node.left), height(node.right));
    }
```

---
title: "[Facebook] Print a Binary Tree in Vertical Order "
category: Question
tags: []
comments: true
date: 2014-12-17 00:00
---


### Question 

[link](http://www.geeksforgeeks.org/print-binary-tree-vertical-order/)

> Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

               1
            /    \
           2      3
          / \    / \
         4   5  6   7
                 \   \
                  8   9 

    The output of print this tree vertically will be:
    4
    2
    1 5 6
    3 8
    7
    9 

### Solution

1. Traverse the tree once and get the minimum and maximum horizontal distance with respect to root. 

2. Iterate the tree and for each vertical line, fill in the values.  

Now, getting the width of tree requires O(n) time. And entire solution is O(n) using a __[HashMap](www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/)__. 

### Code

    public List<List<Integer>> printVertically(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        // 1. find the range of left bound and right bound
        int[] range = new int[2];
        findRange(root, range, 0);

        // 2. calculate number of columns in the result
        int rootIndex = 0 - range[0];
        int columns = range[1] - range[0] + 1;
        for (int i = 0; i < columns; i++) {
            ans.add(new ArrayList<Integer>());
        }
        
        // 3. fill in vertically in a recursive manner
        fillNode(ans, root, rootIndex);

        return ans;
    }

    private void fillNode(List<List<Integer>> ans, TreeNode node, int index) {
        if (node == null) {
            return;
        }
        ans.get(index).add(node.val);
        fillNode(ans, node.left, index - 1);
        fillNode(ans, node.right, index + 1);
    }

    private void findRange(TreeNode node, int[] range, int position) {
        if (node == null) {
            return;
        }
        if (position < range[0]) {
            range[0] = position;
        }
        if (position > range[1]) {
            range[1] = position;
        }
        findRange(node.left, range, position - 1);
        findRange(node.right, range, position + 1);
    }

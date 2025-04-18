---
title: 987. Vertical Order Traversal of a Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-15 00:33
---



Link: https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/

# Question

difficulty: hard
adj diff: 3

	Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

	For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

	The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

	Return the vertical order traversal of the binary tree.

	 

	Example 1:

	Input: root = [3,9,20,null,null,15,7]
	Output: [[9],[3,15],[20],[7]]
	Explanation:
	Column -1: Only node 9 is in this column.
	Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
	Column 1: Only node 20 is in this column.
	Column 2: Only node 7 is in this column.

	Example 2:

	Input: root = [1,2,3,4,5,6,7]
	Output: [[4],[2],[1,5,6],[3],[7]]
	Explanation:
	Column -2: Only node 4 is in this column.
	Column -1: Only node 2 is in this column.
	Column 0: Nodes 1, 5, and 6 are in this column.
			  1 is at the top, so it comes first.
			  5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
	Column 1: Only node 3 is in this column.
	Column 2: Only node 7 is in this column.

	Example 3:

	Input: root = [1,2,3,4,6,5,7]
	Output: [[4],[2],[1,5,6],[3],[7]]
	Explanation:
	This case is the exact same as example 2, but with nodes 5 and 6 swapped.
	Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

	 

	Constraints:

		The number of nodes in the tree is in the range [1, 1000].
		0 <= Node.val <= 1000

这题不难。其实以前做过。

那就是 https://mar2ndx.github.io/2014/12/17/Print-Binary-Tree-Vertically/

不过这道题不能 DFS写，我改成 BFS了，修改不大，如下。

# Code

```
class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
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
        List<TreeNode> list1 = new LinkedList<TreeNode>();
        List<Integer> list2 = new LinkedList<Integer>();
        list1.add(root);
        list2.add(rootIndex);
        while (!list1.isEmpty()) {
            for (int i = list1.size() - 1; i >= 0; i--) {
                TreeNode node = list1.remove(0);
                int curIndex = list2.remove(0);
                ans.get(curIndex).add(node.val);
                if (node.left != null) {
                    list1.add(node.left);
                    list2.add(curIndex - 1);
                }
                if (node.right != null) {
                    list1.add(node.right);
                    list2.add(curIndex + 1);
                }
            }
        }
        return ans;
    }

    private void findRange(TreeNode node, int[] range, int position) {
        if (node == null) return;
        if (position < range[0]) {
            range[0] = position;
        } else if (position > range[1]) {
            range[1] = position;
        }
        findRange(node.left, range, position - 1);
        findRange(node.right, range, position + 1);
    }
}
```

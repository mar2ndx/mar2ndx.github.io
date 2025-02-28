---
title: "[LeetCode 109] Convert Sorted List to Binary Search Tree"
category: Leetcode
tags: []
comments: true
date: 2014-05-26 00:00
---


### Question

[link](https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

<div class="question-content">
            <p></p><p>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</p><p></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Frequency</td>
		<td bgcolor="yellow">3</td>
	</tr>
	<tr>
		<td>Difficulty</td>
		<td bgcolor="red">4</td>
	</tr>
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="red">4</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="red">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**This is a very interesting question, with a very tricky solution**. Because **LinkedList does not have radom access**, it is impossible for us to solve it in like we did in last question.

**The traditional top-down approach** is heavily relied on index operation, and we can't do that. That is why we solve this question with **bottom-up approach**. Which is to say, we insert TreeNodes following LinkedList's order.

I know it's hard to understand. I found a [explanation](http://leetcode.com/2010/11/convert-binary-search-tree-bst-to.html), but it's not clear also. The fastest way is to just read the code or write it by hand.

### Solution

**The key of this solution is a public pointer which traverse thru the list**. Each time the pointer procceed, a new TreeNode is added into the final answer. **How to keep track of parent TreeNodes**? That's the tricky part. we tree structure is generated before the insertion, altough the values have not been filled in yet.

It's like doing a DFS in-order traverse thru the tree, and fill in values one by one. In order to know how the tree would look like, prior knowledge of the size of the LinkedList is necessary.

That's the solution. I've never seen a solution like this before, so it's very important to learn it and memorize it by heart.

### Code

**standard solution**

    ListNode cur = null;

    public TreeNode sortedListToBST(ListNode head) {
        cur = head;
        int k = 0;
        ListNode temp = head;
        while (temp != null) {
            temp = temp.next;
            k ++;
        }
        return helper(0, k - 1);
    }

    private TreeNode helper(int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode head = new TreeNode(-1);
        head.left  = helper(left, mid - 1);
        head.val = cur.val;
        cur = cur.next;
        head.right = helper(mid + 1, right);
        return head;
    }

---
title: "[NineChap 4.2] Linked List Additional"
category: NineChap
tags: []
comments: true
date: 2014-06-18 00:00
---


## Question list

1. **[Union and Intersection of two Linked Lists](/question/2014-06-17-Union-and-intersection-of-linked-list)**

1. **[Insertion Sort List](/leetcode/2014-05-30-Insertion-Sort-List)** - difficult

1. **[Flatten Binary Tree to Linked List](/leetcode/2014-05-28-Flatten-Binary-Tree-to-Linked-List)**

1. **[Convert Sorted List to Binary Search Tree](/leetcode/2014-05-26-Convert-Sorted-List-to-Binary-Search-Tree)**

1. **[Rotate List](/leetcode/2014-05-19-Rotate-List)**

1. **[Remove Nth Node From End of List](/leetcode/2014-05-02-Remove-Nth-Node-From-End-of-List)**

1. **[LRU Cache ](/leetcode/2014-06-03-LRU-Cache)**

1. **[Reverse Nodes in k-Groups](/leetcode/2014-05-11-Reverse-Nodes-in-k-Group)**

1. **[Swap Nodes in Pairs](/leetcode/2014-05-09-Swap-Nodes-in-Pairs)**

## Code

**Union and Intersection of two Linked Lists**

Think about the idea only.

**Insertion Sort List**

    public ListNode insertionSortList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode dummy = new ListNode(0);
        ListNode cur = head;
        while (cur != null) {
            // insert cur into correct pos
            ListNode pos = dummy;
            while (pos.next != null && pos.next.val < cur.val) {
                pos = pos.next;
            }
            ListNode temp = cur.next;
            cur.next = pos.next;
            pos.next = cur;
            cur = temp;
        }
        return dummy.next;
    }

**Flatten Binary Tree to Linked List**

I forgot to set "root.left = null" again, which result in long-time debugging. This is a very common and very silly mistake that I really should avoid.

    public void flatten(TreeNode root) {
        root = helper(root);
    }

    private TreeNode helper(TreeNode node) {
        if (node == null) {
            return null;
        } else if (node.left == null && node.right == null) {
            return node;
        } else if (node.left == null) {
            return helper(node.right);
        } else if (node.right == null) {
            node.right = node.left;
            node.left = null;
            return helper(node.right);
        } else {
            TreeNode tempRight = node.right;
            node.right = node.left;
            node.left = null;
            TreeNode leftTail = helper(node.right);
            leftTail.right = tempRight;
            return helper(tempRight);
        }
    }

**Convert Sorted List to Binary Search Tree**

This is the Mock Interview question. My solution is:

    public TreeNode sortedListToBST(ListNode listHead) {
        if (listHead == null) {
            return null;
        }
        if (listHead.next == null) {
            return new TreeNode(listHead.val);
        }
        ListNode listFirstHalf = listHead;
        ListNode listPreMid = findMiddle(listHead);
        ListNode listSecondHalf = null;
        if (listPreMid.next != null) {
            listSecondHalf = listPreMid.next.next;
        }
        TreeNode head = new TreeNode(listPreMid.next.val);
        listPreMid.next = null;
        head.left = sortedListToBST(listFirstHalf);
        head.right = sortedListToBST(listSecondHalf);
        return head;
    }

    private ListNode findMiddle(ListNode listHead) {
        if (listHead == null) {
            return null;
        }
        ListNode slow = listHead;
        ListNode fast = listHead.next;
        while (fast != null && fast.next != null&& fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

This is not a good answer, cuz I have to findMid in each recursion.

The best solution is, use a global variable and 2 numbers to simplify this process. Code:

    ListNode cur = null;

    public TreeNode sortedListToBST(ListNode head) {
    	if (head == null) {
    		return null;
    	}
    	cur = head;
    	int k = 0;
    	ListNode p = head;
    	while (p != null) {
    		k++;
    		p = p.next;
    	}
    	return build(0, k - 1);
    }

    private TreeNode build(int start, int end) {
    	if (start > end) {
    		return null;
    	}
    	int mid = start + (end - start) / 2;
    	TreeNode leftBranch = build(start, mid - 1);
    	TreeNode head = new TreeNode(cur.val);
    	cur = cur.next;
    	head.left = leftBranch;
    	head.right = build(mid + 1, end);
    	return head;
    }

**Rotate List**

Naive solution:

    public ListNode rotateRight(ListNode head, int n) {
        if (head == null) {
            return null;
        }
        ListNode p = head;
        for (int i = 0; i < n; i++) {
            if (p.next == null) {
                p = head;
            } else {
                p = p.next;
            }
        }
    	ListNode q = head;
    	while (p.next != null) {
    		p = p.next;
    		q = q.next;
    	}
    	p.next = head;
    	ListNode newHead = q.next;
    	q.next = null;
    	return newHead;
    }

Make a circular list:

    public ListNode rotateRight(ListNode head, int n) {
        if (head == null) {
            return null;
        }
    	ListNode p = head;
    	int k = 1;
    	while (p.next != null) {
    		k++;
    		p = p.next;
    	}
    	p.next = head;
    	int steps = k - (n % k);
    	for (int i = 0; i < steps; i++) {
    		p = p.next;
    	}
    	head = p.next;
    	p.next = null;
    	return head;
    }

**Remove Nth Node From End of List**

    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null || n == 0) {
    		return null;
    	}
    	ListNode dummy = new ListNode(0);
    	dummy.next = head;
    	ListNode right = dummy;
    	for (int i = 0; i < n; i++) {
    		right = right.next;
    	}
    	ListNode left = dummy;
    	while (right.next != null) {
    		left = left.next;
    		right = right.next;
    	}
    	left.next = left.next.next;
    	return dummy.next;
    }

**LRU Cache**

I solved it in the original post.

**Reverse Nodes in k-Groups**

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode p = head;
        int count = 0;
        while (p != null) {
            p = p.next;
            count++;
        }
        return helper(head, k, count);
    }

    public ListNode helper(ListNode head, int k, int count) {
        if (head == null || k < 1 || count < k) {
            return head;
        }
        ListNode result = null;
        ListNode cur = head;
        for (int i = 0; i < k; i++) {
            if (cur == null) break;
            ListNode temp = cur.next;
            cur.next = result;
            result = cur;
            cur = temp;
        }
        head.next = helper(cur, k, count - k);
        return result;
    }

**Swap Nodes in Pairs**

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode result = head.next;
        ListNode temp = head.next.next;
        result.next = head;
        head.next = swapPairs(temp);
        return result;
    }

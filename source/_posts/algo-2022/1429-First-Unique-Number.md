---
title: 1429. First Unique Number
category: Leetcode
tags: []
comments: true
date: 2022-11-18 06:34
---


Link: https://leetcode.cn/problems/first-unique-number/

# Question

difficulty: mid
adj diff: 3

	You have a queue of integers, you need to retrieve the first unique integer in the queue.

	Implement the FirstUnique class:

		FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
		int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
		void add(int value) insert value to the queue.

	Example 1:

	Input: 
	["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
	[[[2,3,5]],[],[5],[],[2],[],[3],[]]
	Output: 
	[null,2,null,2,null,3,null,-1]
	Explanation: 
	FirstUnique firstUnique = new FirstUnique([2,3,5]);
	firstUnique.showFirstUnique(); // return 2
	firstUnique.add(5);            // the queue is now [2,3,5,5]
	firstUnique.showFirstUnique(); // return 2
	firstUnique.add(2);            // the queue is now [2,3,5,5,2]
	firstUnique.showFirstUnique(); // return 3
	firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
	firstUnique.showFirstUnique(); // return -1

	Example 2:

	Input: 
	["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
	[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
	Output: 
	[null,-1,null,null,null,null,null,17]
	Explanation: 
	FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
	firstUnique.showFirstUnique(); // return -1
	firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
	firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
	firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
	firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
	firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
	firstUnique.showFirstUnique(); // return 17

	Example 3:

	Input: 
	["FirstUnique","showFirstUnique","add","showFirstUnique"]
	[[[809]],[],[809],[]]
	Output: 
	[null,809,null,-1]
	Explanation: 
	FirstUnique firstUnique = new FirstUnique([809]);
	firstUnique.showFirstUnique(); // return 809
	firstUnique.add(809);          // the queue is now [809,809]
	firstUnique.showFirstUnique(); // return -1

	Constraints:

		1 <= nums.length <= 10^5
		1 <= nums[i] <= 10^8
		1 <= value <= 10^8
		At most 50000 calls will be made to showFirstUnique and add.

这道题跟 LRU Cache 解法一样。所以省略了。

[官方解法如下](https://leetcode.cn/problems/first-unique-number/solution/by-fervent-nashwxk-ywtc/) ：

> 1. 维护一个双头链表，记录目前为止的unique numbers
> 1. 维护一个哈希表，记录每个unique number对应的双头链表节点
> 1. 维护一个set，记录之前已经出现的number

# Code

不是我写的。

```
class FirstUnique {

    private class DoublyLinkedListNode {
        int key;
        DoublyLinkedListNode next, prev;
        DoublyLinkedListNode(int key) {
            this.key = key;
        }
    }

    DoublyLinkedListNode dummyHead, dummyTail;
    Set<Integer> alreadyAppearedNumbers;
    Map<Integer, DoublyLinkedListNode> num2node;

    public FirstUnique(int[] nums) {
        dummyHead = new DoublyLinkedListNode(-1);
        dummyTail = new DoublyLinkedListNode(-1);
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
        alreadyAppearedNumbers = new HashSet<>();
        num2node = new HashMap<>();

        for (int num: nums) {
            add(num);
        }
    }
    
    public int showFirstUnique() {
        if (dummyHead.next == dummyTail) {
            return -1;
        }
        return dummyHead.next.key;
    }
    
    public void add(int value) {
        DoublyLinkedListNode node = num2node.getOrDefault(value, null);
        if (node != null) {
            node.next.prev = node.prev;
            node.prev.next = node.next;
            alreadyAppearedNumbers.add(value);
            num2node.remove(value);
        } else if (!alreadyAppearedNumbers.contains(value)){
            DoublyLinkedListNode newNode = new DoublyLinkedListNode(value);
            num2node.put(value, newNode);
            newNode.prev = dummyTail.prev;
            newNode.next = dummyTail;
            dummyTail.prev.next = newNode;
            dummyTail.prev = newNode;
        }
    }
}
```

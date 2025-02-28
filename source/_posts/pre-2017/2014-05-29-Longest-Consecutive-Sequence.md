---
title: "[LeetCode 128] Longest Consecutive Sequence"
category: Leetcode
tags: []
comments: true
date: 2014-05-29 00:00
---


### Question

[link](https://oj.leetcode.com/problems/longest-consecutive-sequence/)

<div class="question-content">
            <p></p><p>
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
</p>
<p>
For example,<br>
Given <code>[100, 4, 200, 1, 3, 2]</code>,<br>
The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Return its length: <code>4</code>.
</p>
<p>
Your algorithm should run in O(<i>n</i>) complexity.
</p><p></p>
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
		<td bgcolor="lime">just coding is easy</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**I did not solve this question**. We are going to make use of **HashSet**.

Information on HashSet from [official document](http://docs.oracle.com/javase/7/docs/api/java/util/HashSet.html):

> **java.util.HashSet**

> This class **implements the Set interface**, backed by a **hash table** (actually a HashMap instance). It makes no guarantees as to the **iteration order** of the set; in particular, it does not guarantee that the order will remain constant over time. This class permits the **null element**.

> This class offers **constant time performance** for the basic operations (add, remove, contains and size), assuming the hash function disperses the elements properly among the buckets. Iterating over this set requires time proportional to the sum of the HashSet instance's size (the number of elements) plus the "capacity" of the backing HashMap instance (the number of buckets). Thus, it's very important not to set the initial capacity too high (or the load factor too low) if iteration performance is important.

> Note that this implementation is **not synchronized**. If multiple threads access a hash set concurrently, and at least one of the threads modifies the set, it must be synchronized externally.

**To summarize it, HashSet**:

1. implements Set interface

2. implemented by using a hash table

3. un-ordered

4. add, remove and contains methods have constant time O(1)

5. can have null element

6. not sync

### Solution

**Well explained in [this site](http://stackoverflow.com/a/7453295)**.

> Dump everything to a hash set.

> Now go through the hashset. For each element, look up the set for all values neighboring the current value. Keep track of the largest sequence you can find, while removing the elements found from the set. Save the count for comparison.

> Repeat this until the hashset is empty.

> Assuming lookup, insertion and deletion are O(1) time, this algorithm would be O(N) time.

**Updated on July 4th, 2014**: Look at the 2nd for-loop. Here if I do 'for (Integer in: set)' to iterate all numbers, I will get "java.util.ConcurrentModificationException ". This is because we are iterating while modifying. **The most tricky part of this solution is iteration thru the array**, instead of the set. Take note of that!

### Code

```
    public int longestConsecutive(int[] num) {
        int longest = 1;
        HashSet<Integer> set = new HashSet<Integer>();
        for (Integer in: num) set.add(in);
        for (Integer in: num) {
            int left = in - 1, right = in + 1;
            while (set.contains(left)) {
                set.remove(left);
                left --;
            }
            while (set.contains(right)) {
                set.remove(right);
                right ++;
            }
            longest = Math.max(longest, right - left - 1);
        }
        return longest;
    }
```

**Updated Oct 29, 2022**

一定要注意：for loop 里面，iterate array（然后 remove from HashSet）

不要 iterate HashSet！会报错。

```
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i: nums) {
            set.add(i);
        }
        int len = 0;
        for (int j: nums) {
            if (set.contains(j)) {
                int left = j-1, right = j+1;
                while (set.contains(left)) {
                    set.remove(left--);
                }
                while (set.contains(right)) {
                    set.remove(right++);
                }
                len = Math.max(len, right - left - 1);
            }
        }
        return len;
    }
```

其实，官方有一种**不会超时，也不用 hashset.remove()**的代码。如下：

```
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set = new HashSet<Integer>();
        for (int num : nums) {
            num_set.add(num);
        }

        int longestStreak = 0;

        for (int num : num_set) {
            // 注意看：这是 left boundary，所以只需要 right direction check
            // 这样就不会超时了。
            if (!num_set.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (num_set.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
```

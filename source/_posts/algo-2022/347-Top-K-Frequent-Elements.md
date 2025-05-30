---
title: 347. Top K Frequent Elements
category: Leetcode
tags: []
comments: true
date: 2022-12-01 21:50
---



Link: https://leetcode.cn/problems/top-k-frequent-elements/

# Question

difficulty: mid
adj diff: 3

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    
     
    
    Example 1:
    
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
    Example 2:
    
    Input: nums = [1], k = 1
    Output: [1]
    
     
    
    Constraints:
    
        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
    
     
    
    Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Code

```
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i: nums) {
            map.put(i,
                map.getOrDefault(i, 0) + 1
            );
        }

        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(new Comparator<Integer>() {
            public int compare(Integer m, Integer n) {
                return map.get(m) - map.get(n);
            }
        });

        for (int i: map.keySet()) {
            heap.offer(i);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = heap.poll();
        }
        return ans;
    }
}
```

---
title: 692. Top K Frequent Words
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---


Link: https://leetcode.cn/problems/top-k-frequent-words/

# Question

difficulty: mid
adj diff: 4

    Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

    Example 1:

    Input: words = ["i","love","leetcode","i","love","coding"], k = 2
    Output: ["i","love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

    Example 2:

    Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
    Output: ["the","is","sunny","day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

    Constraints:

    	1 <= words.length <= 500
    	1 <= words[i].length <= 10
    	words[i] consists of lowercase English letters.
    	k is in the range [1, The number of unique words[i]]

    Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

这道题主要考察的 java 基础只是，算法没啥可说，min-heap。

我没写完，以下代码不 pass，但是其实也差不多了（差一个 Comparator）。

# Code

```
    public List<String> topKFrequent(String[] words, int k) {
        int len = words.length;
        PriorityQueue<String> heap = new PriorityQueue<String>(k);
        int threshold = 0;

        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String str: words) {
            if (!map.containsKey(str)) {
                map.put(str, 0);
            }
            int count = map.get(str) + 1;
            map.put(str, count);
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String word = entry.getKey();
            int count = entry.getValue();

            if (heap.size() < k) {
                heap.offer(word);
                threshold = Math.min(threshold, count);
            } else {
                if (count > threshold || (count == threshold && word.compareTo(heap.peek()) < 0)) {
                    heap.poll();
                    heap.offer(word);
                    threshold = count;
                }
            }
        }

        List<String> ans = new LinkedList<String>();
        while (heap.size() > 0) {
            ans.add(heap.poll());
        }
        return ans;
    }
```

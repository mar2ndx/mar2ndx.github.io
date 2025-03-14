---
title: 244. Shortest Word Distance II
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:41
---



Link: https://leetcode.cn/problems/shortest-word-distance-ii/

# Question

difficulty: mid
adj diff: 3

    Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

    Implement the WordDistance class:

        WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
        int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

    Example 1:

    Input
    ["WordDistance", "shortest", "shortest"]
    [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    Output
    [null, 3, 1]

    Explanation
    WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
    wordDistance.shortest("coding", "practice"); // return 3
    wordDistance.shortest("makes", "coding");    // return 1

    Constraints:

        1 <= wordsDict.length <= 3 * 104
        1 <= wordsDict[i].length <= 10
        wordsDict[i] consists of lowercase English letters.
        word1 and word2 are in wordsDict.
        word1 != word2
        At most 5000 calls will be made to shortest.

哈希 + 双指针。

# Code

```
class WordDistance {

    Map<String, List<Integer>> map = new HashMap<String, List<Integer>>();

    public WordDistance(String[] wordsDict) {
        for (int i = 0; i < wordsDict.length; i++) {
            List<Integer> list = map.getOrDefault(wordsDict[i], new LinkedList<Integer>());
            list.add(i);
            map.put(wordsDict[i], list);
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int p = 0, q = 0;
        int distance = Integer.MAX_VALUE;
        while (p < list1.size() && q < list2.size()) {
            distance = Math.min(distance, Math.abs(list1.get(p) - list2.get(q)));
            if (list1.get(p) < list2.get(q)) {
                p++;
            } else {
                q++;
            }
        }
        return distance;
    }
}
```

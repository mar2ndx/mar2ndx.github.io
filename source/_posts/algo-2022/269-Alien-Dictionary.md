---
title: 269. Alien Dictionary
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/alien-dictionary/

# Question

difficulty: hard
adj diff: 5

    There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

    You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

    Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

    A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

    Example 1:

    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"
    Example 2:

    Input: words = ["z","x"]
    Output: "zx"
    Example 3:

    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".

    Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.

这道题，是标准的拓扑排序题。

难点在于，需要用给定的 words list，先 build 一个 graph。

然后就是标准的一个 queue，添加 0 入 节点，然后 bfs 排序。

# Code

参考别人的代码写的 BFS，比较长：

```
    public String alienOrder(String[] words) {
        if(words == null || words.length == 0){
          return "";
        }

        // neighbor represent the list of next nodes
        Map<Character, Set<Character>> neighbors = new HashMap<>();
        // indegrees represent how many dependent nodes
        Map<Character, Integer> indegrees = new HashMap<>();

        // eg. 'a' 'b' 'c' ==>
        // neighbors = {'a' -> ['b', 'c'] }
        //           = {'b' -> ['c'] }
        //           = {'c' -> [] }
        // indegrees = { 'a' = 0, 'b' = 1, 'c' = 2}

        // initialize neighbors and indegree
        for (int i = 0; i < words.length; i++){
            for(int j = 0; j < words[i].length(); j++){
                char ch = words[i].charAt(j);
                if (!neighbors.containsKey(ch)) {
                    neighbors.put(ch, new HashSet<Character>());
                }
                indegrees.put(ch, 0);
            }
        }

        // 查看所有相近 chars，放入neighbors的 HashSet
        for (int i = 0; i + 1 < words.length; i++){
            int p = 0;
            int len = Math.min(words[i].length(), words[i + 1].length());
            while (p < len) {
                char first = words[i].charAt(p);
                char second = words[i + 1].charAt(p);
                if (first != second) {
                    // add first -> second to neighbors and indegrees
                    neighbors.get(first).add(second);
                    break;
                }
                p++;
            }
            if (p == len && words[i].compareTo(words[i + 1]) > 0) {
                // the {"abc", "ab"} case, directly return empty
                return "";
            }
        }

        // build indegrees
        for (char key : neighbors.keySet()) {
            for (char inChar: neighbors.get(key)) {
                indegrees.put(inChar, indegrees.get(inChar) + 1);
            }
        }

        // start the toplogical sorting
        PriorityQueue<Character> queue = new PriorityQueue<>();
        for (char key : indegrees.keySet()){
            if(indegrees.get(key) == 0){
                queue.add(key);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            char cur = queue.remove();
            sb.append(cur);
            for(char neighbor : neighbors.get(cur)){
                int new_indegree = indegrees.get(neighbor) - 1;
                if(new_indegree == 0){
                    queue.add(neighbor);
                }
                indegrees.put(neighbor, new_indegree);
            }
        }

        // 判断排出来的拓扑序是不是有效的, 是不是所有的节点都遍历过了
        // 如果不是的话我们直接输出空串, 证明组成给定的这些单词的字母没有办法组成一个合理的拓扑序
        String finalOrder = sb.toString();
        if (finalOrder.length() < neighbors.keySet().size()){
          return "";
        } else {
            return finalOrder;
        }
    }
```

官方答案，跟简洁一点：https://leetcode.cn/problems/alien-dictionary/solution/huo-xing-ci-dian-by-leetcode-solution-nr0l/

```java
class Solution {
    Map<Character, List<Character>> edges = new HashMap<Character, List<Character>>();
    Map<Character, Integer> indegrees = new HashMap<Character, Integer>();
    boolean valid = true;

    public String alienOrder(String[] words) {
        int length = words.length;
        for (String word : words) {
            int wordLength = word.length();
            for (int j = 0; j < wordLength; j++) {
                char c = word.charAt(j);
                edges.putIfAbsent(c, new ArrayList<Character>());
            }
        }
        for (int i = 1; i < length && valid; i++) {
            addEdge(words[i - 1], words[i]);
        }
        if (!valid) {
            return "";
        }
        Queue<Character> queue = new ArrayDeque<Character>();
        Set<Character> letterSet = edges.keySet();
        for (char u : letterSet) {
            if (!indegrees.containsKey(u)) {
                queue.offer(u);
            }
        }
        StringBuffer order = new StringBuffer();
        while (!queue.isEmpty()) {
            char u = queue.poll();
            order.append(u);
            List<Character> adjacent = edges.get(u);
            for (char v : adjacent) {
                indegrees.put(v, indegrees.get(v) - 1);
                if (indegrees.get(v) == 0) {
                    queue.offer(v);
                }
            }
        }
        return order.length() == edges.size() ? order.toString() : "";
    }

    public void addEdge(String before, String after) {
        int length1 = before.length(), length2 = after.length();
        int length = Math.min(length1, length2);
        int index = 0;
        while (index < length) {
            char c1 = before.charAt(index), c2 = after.charAt(index);
            if (c1 != c2) {
                edges.get(c1).add(c2);
                indegrees.put(c2, indegrees.getOrDefault(c2, 0) + 1);
                break;
            }
            index++;
        }
        if (index == length && length1 > length2) {
            valid = false;
        }
    }
}
```

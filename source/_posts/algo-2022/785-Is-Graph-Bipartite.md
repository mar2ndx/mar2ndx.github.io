---
title: 785. Is Graph Bipartite?
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---


Link: https://leetcode.cn/problems/is-graph-bipartite/

# Question

difficulty: mid
adj diff: 5

    There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

    	There are no self-edges (graph[u] does not contain u).
    	There are no parallel edges (graph[u] does not contain duplicate values).
    	If v is in graph[u], then u is in graph[v] (the graph is undirected).
    	The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

    A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

    Return true if and only if it is bipartite.

    Example 1:

    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

    Example 2:

    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

    Constraints:

    	graph.length == n
    	1 <= n <= 100
    	0 <= graph[u].length < n
    	0 <= graph[u][i] <= n - 1
    	graph[u] does not contain u.
    	All the values of graph[u] are unique.
    	If graph[u] contains v, then graph[v] contains u.

这道题的 bfs 搜索，看似不难，但是难在 graph 会有好几个孤岛。

如何处理孤岛，保证全都 visit 一遍，这个很难。

最后是 3 层循环，其中第二层循环之前才创建 queue。这个方法第一次碰到。写起来真费劲。

# Code

```
    public boolean isBipartite(int[][] graph) {
        int len = graph.length;
        int[] visited = new int[len];

        for (int i = 0; i < len; i++) {
            if (visited[i] != 0) {
                continue;
            }
            List<Integer> list = new LinkedList<Integer>();
            list.add(i);
            visited[i] = 1;
            while (!list.isEmpty()) {
                int visitIndex = list.remove(0);
                int nextValue = 3 - visited[visitIndex];
                for (int visitNext: graph[visitIndex]) {
                    // visitNext is adjacent to visitIndex, thus value should = nextValue
                    if (visited[visitNext] == nextValue) {
                        continue;
                    } else if (visited[visitNext] == 0) {
                        visited[visitNext] = nextValue;
                        list.add(visitNext);
                    } else if (visited[visitNext] != nextValue) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
```

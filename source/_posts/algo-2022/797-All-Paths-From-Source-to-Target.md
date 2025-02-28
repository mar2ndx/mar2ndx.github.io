---
title: 797. All Paths From Source to Target
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---



Link: https://leetcode.cn/problems/all-paths-from-source-to-target/

# Question

difficulty: mid
adj diff: 3

    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

    Example 1:

    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

    Example 2:

    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

    Constraints:

    n == graph.length
    2 <= n <= 15
    0 <= graph[i][j] < n
    graph[i][j] != i (i.e., there will be no self-loops).
    All the elements of graph[i] are unique.
    The input graph is guaranteed to be a DAG.

# Code

```
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> ans = new LinkedList<List<Integer>>();
        int n = graph.length;
        boolean[] visited = new boolean[n];
        List<Integer> path = new LinkedList<Integer>();
        path.add(0);
        visited[0] = true;
        helper(ans, path, visited, graph, n - 1);
        return ans;
    }

    private void helper(List<List<Integer>> ans, List<Integer> path,
            boolean[] visited, int[][] graph, int target) {
        int lastNode = path.get(path.size() - 1);
        if (lastNode == target) {
            ans.add(new LinkedList<Integer>(path));
            return;
        }

        for (Integer i: graph[lastNode]) {
            if (visited[i] == false) {
                visited[i] = true;
                path.add(i);
                helper(ans, path, visited, graph, target);
                visited[i] = false;
                path.remove(path.size() - 1);
            }
        }
    }
```

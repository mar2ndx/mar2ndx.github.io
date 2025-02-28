---
title: 261. Graph Valid Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/graph-valid-tree/

# Question

difficulty: hard
adj diff: 4

    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

    Return true if the edges of the given graph make up a valid tree, and false otherwise.	 
    Example 1:

    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

    Example 2:

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false

    Constraints:

    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no self-loops or repeated edges.

并查集问题。（参考另一篇帖子，这里先不讨论并查集）

但是也可以用 dfs/bfs 来做。

只需要保证 3 点：

1. n 个 node，一定是对应(n-1)个 edge
2. 无环
3. 无孤岛（所有的 node 都能通过 bfs/dfs 访问一遍）

代码如下：

# Code

BFS（注意这段代码，通过双向 directed edge 来判断 circle 的逻辑）

```
    public boolean validTree(int n, int[][] edges) {
        //构建邻接矩阵
        int[][] graph = new int[n][n];
        //有边的元素设置为1，没有边的元素设置为0
        for (int[] edge : edges) {
            graph[edge[0]][edge[1]] = 1;
            graph[edge[1]][edge[0]] = 1;
        }
        //进行BFS
        Queue<Integer> queue = new LinkedList<>();
        //从第一个节点开始搜索，这样就不会漏掉无边图的情况
        queue.add(0);
        boolean[] visited = new boolean[n];
        while (!queue.isEmpty()) {
            Integer cur = queue.poll();
            visited[cur] = true;
            //获取邻接点
            for (int i = 0; i < n; i++) {
                //查看当前节点的邻接点
                if (graph[cur][i] == 1) {
                    //如果访问过，则返回false
                    if (visited[i])
                        return false;

                    //标记邻接点，入队列
                    visited[i] = true;
                    //涂黑访问过的节点
                    graph[cur][i] = 0;
                    graph[i][cur] = 0;
                    queue.add(i);
                }
            }
        }

        //判断是否为单连通分量
        for (int i = 0; i < n; i++) {
            if (!visited[i])
                return false;
        }
        return true;
    }
```

DFS（注意这段代码，只判断 n-1edges，以及孤岛，没有判断 circle。也是 work 的）

```
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        int[] out = new int[n];
        int cnt = 0;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n; ++i){
            graph.add(new ArrayList<>());
        }
        for(int[] arr: edges){
            out[arr[0]]++;
            out[arr[1]]++;
            graph.get(arr[0]).add(arr[1]);
            graph.get(arr[1]).add(arr[0]);
        }
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < out.length; ++i){
            if(out[i] == 1) queue.add(i);
        }
        while(!queue.isEmpty()){
            int size = queue.size();
            cnt += size;
            for(int s = 0; s < size; ++s){
                int temp = queue.poll();
                for(int num : graph.get(temp)){
                    if(--out[num] == 1) queue.add(num);
                }
            }
        }
        return cnt == n || (n == 1 && edges.length == 0);
    }
```

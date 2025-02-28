---
title: 547. Number of Provinces
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/number-of-provinces/

# Question

difficulty: mid
adj diff: 3

    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.
    Example 1:

    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

    Example 2:

    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Constraints:

    	1 <= n <= 200
    	n == isConnected.length
    	n == isConnected[i].length
    	isConnected[i][j] is 1 or 0.
    	isConnected[i][i] == 1
    	isConnected[i][j] == isConnected[j][i]

这道题不难，只要考察 bfs 代码的数量城都。

一次过。

# Code

```
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int count = 0;
        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<Integer>();

        while (true) {
            // 1. find a un-visited node from all nodes
            for (int i = 0; i < n; i++) {
                if (visited[i] == false) {
                    q.add(i);
                    count++;
                    visited[i] = true;
                    break;
                }
            }

            // 2. start BFS using the node above
            if (q.isEmpty()) {
                break;
            } else {
                // mark all adjacent nodes are visited
                while (!q.isEmpty()) {
                    int cur = q.remove();
                    for (int j = 0; j < n; j++) {
                        if (j != cur && isConnected[j][cur] == 1 && !visited[j]) {
                            q.add(j);
                            visited[j] = true;
                        }
                    }
                }
            }
        }
        return count;
    }
```

实际上，两个 loop 可以合二为一。

如下（别人的代码）：

```
    public int findCircleNum(int[][] isConnected) {
        int cities = isConnected.length;
        boolean[] visited = new boolean[cities];
        int provinces = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < cities; i++) {
            if (!visited[i]) {
                queue.offer(i);
                while (!queue.isEmpty()) {
                    int j = queue.poll();
                    visited[j] = true;
                    for (int k = 0; k < cities; k++) {
                        if (isConnected[j][k] == 1 && !visited[k]) {
                            queue.offer(k);
                        }
                    }
                }
                provinces++;
            }
        }
        return provinces;
    }
```

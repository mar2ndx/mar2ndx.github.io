---
title: 773. Sliding Puzzle
category: Leetcode
tags: []
comments: true
date: 2022-11-09 18:36
---


Link: https://leetcode.cn/problems/sliding-puzzle/

# Question

difficulty: hard
adj diff: 4

    On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

    The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

    Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

    Example 1:

    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.

    Example 2:

    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.

    Example 3:

    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.

        An example path:
        After move 0: [[4,1,2],[5,0,3]]
        After move 1: [[4,1,2],[0,5,3]]
        After move 2: [[0,1,2],[4,5,3]]
        After move 3: [[1,0,2],[4,5,3]]
        After move 4: [[1,2,0],[4,5,3]]
        After move 5: [[1,2,3],[4,5,0]]

    Constraints:

    	board.length == 2
    	board[i].length == 3
    	0 <= board[i][j] <= 5
    	Each value board[i][j] is unique.

这道题代码量很大，但是就是基本的 bfs （用一个 queue 一个 visited map）。

# Code

代码不是我写的。

```
    int[][] neighbors = {{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};

    public int slidingPuzzle(int[][] board) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                sb.append(board[i][j]);
            }
        }
        String initial = sb.toString();
        if ("123450".equals(initial)) {
            return 0;
        }

        int step = 0;
        Queue<String> queue = new LinkedList<String>();
        queue.offer(initial);
        Set<String> seen = new HashSet<String>();
        seen.add(initial);

        while (!queue.isEmpty()) {
            ++step;
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                String status = queue.poll();
                for (String nextStatus : get(status)) {
                    if (!seen.contains(nextStatus)) {
                        if ("123450".equals(nextStatus)) {
                            return step;
                        }
                        queue.offer(nextStatus);
                        seen.add(nextStatus);
                    }
                }
            }
        }

        return -1;
    }

    // 枚举 status 通过一次交换操作得到的状态
    public List<String> get(String status) {
        List<String> ret = new ArrayList<String>();
        char[] array = status.toCharArray();
        int x = status.indexOf('0');
        for (int y : neighbors[x]) {
            swap(array, x, y);
            ret.add(new String(array));
            swap(array, x, y);
        }
        return ret;
    }

    public void swap(char[] array, int x, int y) {
        char temp = array[x];
        array[x] = array[y];
        array[y] = temp;
    }
```

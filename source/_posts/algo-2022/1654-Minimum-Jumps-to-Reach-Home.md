---
title: 1654. Minimum Jumps to Reach Home
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/minimum-jumps-to-reach-home/

# Question

difficulty: mid
adj diff: 4

    A certain bug's home is on the x-axis at position x. Help them get there from position 0.

    The bug jumps according to the following rules:

    	It can jump exactly a positions forward (to the right).
    	It can jump exactly b positions backward (to the left).
    	It cannot jump backward twice in a row.
    	It cannot jump to any forbidden positions.

    The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

    Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

    Example 1:

    Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
    Output: 3
    Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

    Example 2:

    Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
    Output: -1

    Example 3:

    Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
    Output: 2
    Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

    Constraints:

    	1 <= forbidden.length <= 1000
    	1 <= a, b, forbidden[i] <= 2000
    	0 <= x <= 2000
    	All the elements in forbidden are distinct.
    	Position x is not forbidden.

# Code

```
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        Set<Integer> visited = new HashSet<Integer>();
        for (Integer i: forbidden) {
            visited.add(i);
        }

        Queue<GraphNode> queue = new LinkedList<GraphNode>();
        queue.add(new GraphNode(0, false, 0));

        while (!queue.isEmpty()) {
            GraphNode nextNode = queue.poll();
            if (nextNode.pos == x) {
                return nextNode.steps;
            }
            // else: visit nextNode.pos + a and nextNode.pos - b (if true)
            if (nextNode.pos + a <= 6666 && !visited.contains(nextNode.pos + a)) {
                visited.add(nextNode.pos + a);
                queue.offer(new GraphNode(nextNode.pos + a, true, nextNode.steps + 1));
            }
            if (nextNode.pos - b > 0 && !visited.contains(nextNode.pos - b) && nextNode.direction == true) {
                queue.offer(new GraphNode(nextNode.pos - b, false, nextNode.steps + 1));
            }
        }
        return -1;
    }

    class GraphNode {
        int pos;
        boolean direction;
        int steps;

        public GraphNode(int p, boolean toRight, int count) {
            pos = p;
            direction = toRight;
            steps = count;
        }
    }
```

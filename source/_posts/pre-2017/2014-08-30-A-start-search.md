---
title: "[Fundamental] A-Star Search "
category: Fundamental
tags: []
comments: true
date: 2014-08-30 00:00
---


### Definition

A\* is a computer algorithm that is widely used in pathfinding and graph traversal.

It uses a knowledge-plus-heuristic cost function like this:

> f (n) = g(n) + h(n)
>
> f (n): estimated total cost of path through n to goal
>
> g(x) = past path-cost function
>
> h(x) = future path-cost function, which is an admissible "heuristic estimate" of the distance from x to the goal

What sets A\* **apart from a greedy best-first search** is that it also takes the distance already traveled into account.

### Implementation

[Maintains a priority queue](http://en.wikipedia.org/wiki/A*_search_algorithm#Process) (lower f(x) means higher priority). At each step, node with the lowest f(x) value is removed from the queue, and neighbors are added to the queue.

This continues until a goal node has a lower f value than any node in the queue. Goal found!

### Relationship with Dijkstra

**[Dijkstra is a special case](http://stackoverflow.com/a/1332478) for A\*** (when the [heuristics is 0](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm)).

Illustration (A-star):

![](/images/path-find-Astar.gif)

Illustration (Dijkstra's algorithm):

![](/images/path-find-Dijkstras.gif)

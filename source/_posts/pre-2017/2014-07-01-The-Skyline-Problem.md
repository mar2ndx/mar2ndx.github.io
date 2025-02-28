---
title: "[Question] The Skyline Problem"
category: Question
tags: []
comments: true
date: 2014-07-01 00:00
---


## Question

[link](http://www.algorithmist.com/index.php/UVa_105)

> Given n buildings, each building is an rectangle located on
> x-axis, and indicated by (x1, x2, height). Calculate the
> outline of all buildings. Output them in order.

## Solution

**Sweeping Line Algorithm**.

Sweep from left to right, always try to find the largest height of the rectangle.

First make sure the rectangles are sorted. While sweeping, if sees an building-start, insert the height to the heap. If a building-end, remove from the heap. Then the current maximum height is the max point in the heap.

A visualized explanation can be found [here](https://briangordon.github.io/2014/08/the-skyline-problem.html).

Total cost is O(nlogn), [source](http://qr.ae/Yt74m).

另一个很好的 explanation：

At #26 Floor of [this post](http://www.mitbbs.com/article_t1/JobHunting/32569901_0_2.html), we can do insertion and deletion in max-heap, then peek the largest element in the heap.

> 把所有的 turning points 放在一起，根据 coordination 从小到大 sort 。

> 再用 max-heap, 把所有的 turning points 扫一遍，遇到 start turning point, 把 volume 放入 max-heap. 遇到 end turning point，把对应的 volume 从 max-heap 中取出。

> max-heap 的 max 值就是对应区间的最大 volume

### Code

The max-heap solution

```
    public int[] skyline(List<Building> bds, int min, int max) {
    	int[] output = new int[max - min];

    	List<Edge>[] edges = new List[max - min];
    	for (int i = 0; i < edges.length; i++) {
    		edges[i] = new ArrayList<Edge>();
    	}
    	for (Building b : bds) {
    		// put all edges into an array of edges
    		edges[b.from].add(new Edge(b, true));
    		edges[b.to].add(new Edge(b, false));
    	}

    	Queue<Building> heap = new PriorityQueue<Building>(100,
    			new Comparator<Building>() {
    				public int compare(Building b1, Building b2) {
    					return b2.height - b1.height;
    				}
    			});
    	for (int i = 0; i < edges.length; i++) {
    		// insert or remove each building at position i into max heap
    		for (Edge e : edges[i]) {
    			if (e.isEnter) {
    				heap.add(e.building);
    			} else {
    				heap.remove(e.building);
    			}
    		}
    		// then culculate the current hight, which is top of the heap
    		if (!heap.isEmpty()) {
    			output[i] = heap.peek().height;
    		}
    	}

    	return output;
    }

    static class Edge {
    	Building building;
    	boolean isEnter;

    	public Edge(Building bld, boolean enter) {
    		building = bld;
    		isEnter = enter;
    	}
    }

    static class Building {
    	int from;
    	int to;
    	int height;

    	public Building(int a, int b, int c) {
    		from = a;
    		to = b;
    		height = c;
    	}
    }
```

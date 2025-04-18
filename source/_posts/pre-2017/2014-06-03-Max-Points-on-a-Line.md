---
title: "[LeetCode 149] Max Points on a Line"
category: Leetcode
tags: []
comments: true
date: 2014-06-03 00:00
---


### Question

[link](https://oj.leetcode.com/problems/max-points-on-a-line/)

<div class="question-content bg-color bg-img font-color">
            <p class="font-color"></p><p class="font-color">Given <i>n</i> points on a 2D plane, find the maximum number of points that lie on the same straight line.</p><p class="font-color"></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="red">5</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="red">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**This is a difficult coding question**.

The idea is simple. For n points, there are n \* (n-1) lines. Check slopes and then count total, we would get the answer.

However, coding of this idea is very difficult.

### Solution

**Firstly, there are 2 special cases when calculating the slope**. The 2 points may locate in same position. And when point1.x = point2.x, slope = infinity. It's easy to omit these 2 cases and result in mistake.

Secondly, when we count, we declare 2 variables: samePointNumber and maxPointCountWithSameSlope. **It's very important to initialize both values to 1 instead of 0**! Why? Because these values just can't be 0. I failed my 2nd version code when input = {(0,0), (0,0)}, the program shows result of 0, instead of 2.

**Thirdly, about what data structure to use for counting**. There is a discussion about this at [here](https://oj.leetcode.com/discuss/2573/better-way-to-use-hashmap-for-this-question)

> 1. storing the vertical slopes as Double.NaN. That allows Double to represent every slope uniquely as (y/x).
> 2. It is unsafe using floating points to make a hash, and -0.0 != 0.0

It's great that using **Double.NaN**, it saves us time and effort to count vertical points. Second point is very valid, but it turns out that using HashMap<Double, Integer> can AC.

P.S. It is always not a good practise to use Double as hash key. See [here](http://stackoverflow.com/questions/1074781/double-in-hashmap).

**Fourthly, I made a mistake here**:

> double slope = (p.y - q.y) / (p.x - q.x);

And it's wrong. Why? Note that **Point.x and Point.y are both integers**. Integer division will return integer. We must cast it.

> double slope = (double) (p.y - q.y) / (p.x - q.x);

**Last, OMG I wish this is last, but not least, we can reduce execution time to half** by checking only the points with larger index than the anchor point (that's the name for 'current point'). Good idea, right?

One more thing, **how to iterate thru the HashMap** (value only)? There is an easy way:

    for (Integer a : map.values()) {
        a;
    }

That's all I've found for now.

**Updated on Aug 12th, 2014**

Based on the solution given in CC150 v4 Q10.6 on Page 199, it's a **proper way to solve with HashMap<Line, Integer>** instead of using HashMap<Double, Integer>.

The reason is mentioned, it's '**unsafe using floating points to make a hash**'.

Note that if we were to write our own 'Line' class, **we must override the 2 methods**:

1. public int hashCode() {}
1. public boolean equals(Object o) {}

### Code

**written by me, Version3 using HashMap**

    public int maxPoints(Point[] points) {
    	if (points.length <= 1)
    		return points.length;
    	HashMap<Double, Integer> map = null;
    	int totalMax = 0;
    	for (Point p : points) {
    		int samePoint = 1;
    		map = new HashMap<Double, Integer>();
    		for (Point q : points) {
    			if (q == p || p.x > q.x) {
    			} else if (p.x == q.x && p.y == q.y) {
    				samePoint++;
    			} else {
    				double slope = Double.NaN;
    				if (p.x != q.x) {
    					slope = (double) (p.y - q.y) / (p.x - q.x);
    				}
    				if (!map.containsKey(slope)) {
    					map.put(slope, 1);
    				}
    				map.put(slope, map.get(slope) + 1);
    			}
    		}
    		int pointMax = 1;
    		for (Integer a : map.values()) {
    			pointMax = Math.max(pointMax, a);
    		}
    		totalMax = Math.max(totalMax, pointMax + samePoint - 1);
    	}
    	return totalMax;
    }

---
layout: post
title: "[LeetCode 134] Gas Station"
comments: true
category: Leetcode
---

### Question

[link](https://oj.leetcode.com/problems/gas-station/)

<div class="question-content">
            <p class="font-color"></p><p class="font-color">
There are <i>N</i> gas stations along a circular route, where the amount of gas at station <i>i</i> is <code>gas[i]</code>.
</p>

<p class="font-color">
You have a car with an unlimited gas tank and it costs <code>cost[i]</code> of gas to travel from station <i>i</i> to its next station (<i>i</i>+1). You begin the journey with an empty tank at one of the gas stations.
</p>

<p class="font-color">
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
</p>

<p class="font-color">
<b>Note:</b><br>
The solution is guaranteed to be unique.
</p><p class="font-color"></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="red">4</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="yellow">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**This is a tough question, which requires a lot of math-related thinking**.

**My solution is IMHO very simple and easy**. I first do a cumulation of gas from beginning to the end, and find the lowest cumulative value of the gas tank (of course can be negative). That point is where I start the journey, which is to say, I will validate the path from that point, and then return the result.

**This idea is not seen on Internet**, although it is just 2 loops thru the list, and time complexity is also O(n). Anyway, there's a great solution which most people uses.

**There's a great [post](https://oj.leetcode.com/discuss/4159/share-some-of-my-ideas) that gives 2 valid conclusions**:

> 1. If car starts at A and can not reach B (let's say B is the first station that A can not reach), then any station between A and B can not reach B.
> 2. If the total number of gas is bigger than the total number of cost. There must be a valid solution.

From here, a great solution can be found.

### Solution

**A very detailed explanation and code is found from [this blog](http://leetcodenotes.wordpress.com/2013/11/21/leetcode-gas-station-%E8%BD%AC%E5%9C%88%E7%9A%84%E5%8A%A0%E6%B2%B9%E7%AB%99%E7%9C%8B%E8%83%BD%E4%B8%8D%E8%83%BD%E8%B5%B0%E4%B8%80%E5%9C%88/)**.

> 1. 从 i 开始，j 是当前 station 的指针，sum += gas[j] – cost[j] （从 j 站加了油，再算上从 i 开始走到 j 剩的油，走到 j+1 站还能剩下多少油）
> 2. 如果 sum < 0，说明从 i 开始是不行的。那能不能从 i..j 中间的某个位置开始呢？假设能从 k (i <=k<=j)走，那么 i..j < 0，若 k..j >=0，说明 i..k – 1 更是<0，那从 k 处就早该断开了，根本轮不到 j。
> 3. 所以一旦 sum<0，i 就赋成 j + 1，sum 归零。

And note that if i is moved to j, there is no need to check (0..old_i) again, because this range must be reachable (write code again for beter understanding).

Coding this solution **is not easy**! I failed to do it.

### Code

**First, my solution**

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int len = gas.length;
    	if (len == 0) return -1;
    	int start = -1, min = Integer.MAX_VALUE, total = 0;
    	for (int i = 0; i < len; i ++) {
    		total += getDiff(gas, cost, i);
    		if (total < min) {
    			min = total;
    			start = i;
    		}
    	}
    	start = (start + 1) % len;
    	// now traverse the route from start
    	total = 0;
    	for (int i = 0; i < len; i ++) {
    		total += getDiff(gas, cost, (start + i) % len);
    		if (total < 0) return -1;
    	}
    	return start;
    }

    private int getDiff(int[] gas, int[] cost, int i) {
    	return gas[i] - cost[i];
    }

**Second, best solution**

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int i = 0, j = 0;
        int sum = 0;
        int total = 0;
        while (j < gas.length) {
            int diff = gas[j] - cost[j];
            if (sum + diff < 0) {
                i = j + 1;
                sum = 0;
            } else {
                sum += diff;
            }
            j++;
            total += diff;
        }
        return total >= 0 ? i : -1;
    }

Updated Oct 29, 2022

```
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int start = 0;
        while (start < n) {
            int totalGas = 0;
            int totalCost = 0;
            boolean isValidStart = true;
            for (int i = 0; i < n; i++) {
                int index = (start + i) % n;
                totalGas += gas[index];
                totalCost += cost[index];
                if (totalGas < totalCost) {
                    // invalid starting point
                    start += i + 1;
                    isValidStart = false;
                    break;
                }
            }
            if (isValidStart) {
                return start;
            }
        }
        return start >= n ? -1 : start;
    }
```

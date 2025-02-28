---
title: 253. Meeting Rooms II
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---



Link: https://leetcode.cn/problems/meeting-rooms-ii/

# Question

difficulty: mid
adj diff: 3

    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

    Example 1:

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
    Example 2:

    Input: intervals = [[7,10],[2,4]]
    Output: 1

    Constraints:

    1 <= intervals.length <= 104
    0 <= starti < endi <= 106

思路其实不难：那就是，我不在乎 「开始 time - 结束 time」时间的绑定关系。

我只需要知道如下逻辑：

1. 3:10AM 有 meeting 开始了，room++
1. 3:12AM 有 meeting 开始了，room++
1. 3:13AM 有 meeting 结束了，room--
1. 3:15AM 有 meeting 开始了，room++

以下的代码是做了一个新的 data strucuture。

其实完全没必要，两个 array list 就行：one for meeting start_time, one for end_time. 然后双指针扫。

# Code

我的代码。

```
public int minMeetingRooms(int[][] intervals) {
	MeetingTime[] timeList = new MeetingTime[intervals.length * 2];
	int p = 0;
	for (int[] meeting: intervals) {
		timeList[p++] = new MeetingTime(meeting[0], 1);
		timeList[p++] = new MeetingTime(meeting[1], -1);
	}
	Arrays.sort(timeList);
	int roomsRequired = 0;
	int maxRequired = 0;
	for (MeetingTime time: timeList) {
		roomsRequired += time.startOrEnd;
		maxRequired = Math.max(maxRequired, roomsRequired);
	}
	return maxRequired;
}

class MeetingTime implements Comparable<MeetingTime> {
	int time;
	int startOrEnd; // startOrEnd = 1 means start, startOrEnd = -1 means end

	public MeetingTime(int a, int b) {
		time = a;
		startOrEnd = b;
	}

	public int compareTo(MeetingTime m) {
		if (time == m.time) {
			return startOrEnd - m.startOrEnd;
		} else {
			return time - m.time;
		}
	}
}
```

代码思路源自：https://leetcode.cn/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-by-leetcode/

```
    public int minMeetingRooms(int[][] intervals) {
        int len = intervals.length;
        Integer[] startTimeArray = new Integer[len];
        Integer[] endTimeArray = new Integer[len];

        // build startTimeArray and endTimeArray
        for (int i = 0; i < len; i++) {
            startTimeArray[i] = intervals[i][0];
            endTimeArray[i] = intervals[i][1];
        }
        Arrays.sort(startTimeArray);
        Arrays.sort(endTimeArray);

        // 2 pointers: p for startTimeArray, q for endTimeArray
        int p = 0;
        int q = 0;
        int usedRooms = 0;
        int maxRooms = 0;

        while (p < len) {
            if (endTimeArray[q] <= startTimeArray[p]) {
                // a meeting is finished at this time
                usedRooms--;
                q++;
            } else {
                usedRooms++;
                p++;
            }
            maxRooms = Math.max(maxRooms, usedRooms);
        }

        return maxRooms;
    }
```

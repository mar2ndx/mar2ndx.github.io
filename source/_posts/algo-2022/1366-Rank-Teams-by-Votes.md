---
title: 1366. Rank Teams by Votes
category: Leetcode
tags: []
comments: true
date: 2022-10-30 23:08
---



Link: https://leetcode.cn/problems/rank-teams-by-votes/

# Question

difficulty: mid
adj diff: 3

	In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.

	The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

	Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

	Return a string of all teams sorted by the ranking system.

	 

	Example 1:

	Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
	Output: "ACB"
	Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
	Team B was ranked second by 2 voters and was ranked third by 3 voters.
	Team C was ranked second by 3 voters and was ranked third by 2 voters.
	As most of the voters ranked C second, team C is the second team and team B is the third.

	Example 2:

	Input: votes = ["WXYZ","XYZW"]
	Output: "XWYZ"
	Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 

	Example 3:

	Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
	Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
	Explanation: Only one voter so his votes are used for the ranking.

	 

	Constraints:

		1 <= votes.length <= 1000
		1 <= votes[i].length <= 26
		votes[i].length == votes[j].length for 0 <= i, j < votes.length.
		votes[i][j] is an English uppercase letter.
		All characters of votes[i] are unique.
		All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

用到的 data structure 比较多。

主要的思路就是：用一个长度为26的array来代表一个队的得票数。然后自定义 comparator （2种写法：implements Comparator, 或者 implements Comparable）。

其实可以省一个 data structure，在 comparator 种复用一下 map 的数据，就行了。

# Code

```
class Solution {
    public String rankTeams(String[] votes) {
        // there is only 26 positions for each team
        // eg. Team-A = {2, 3, 1, 0, 6, 7}
        // eg. Team-B = {2, 3, 1, 4, 1, 7}
        Map<Character, TeamVotes> map = new HashMap<Character, TeamVotes>();
        for (String s: votes) {
            char[] countVotes = s.toCharArray();
            for (int i = 0; i < countVotes.length; i++) {
                char oneVote = countVotes[i];
                if (!map.containsKey(oneVote)) {
                    map.put(oneVote, new TeamVotes(oneVote));
                }
                map.get(oneVote).votes[i]++;
            }
        }

        // put the map into a list and sort it
        List<TeamVotes> list = new ArrayList<TeamVotes>();
        for (char charKey: map.keySet()) {
            list.add(map.get(charKey));
        }
        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for (TeamVotes tv: list) {
            sb.append(tv.team);
        }
        return sb.toString();
    }

    class TeamVotes implements Comparable<TeamVotes> {
        char team;
        int[] votes;

        public TeamVotes(char teamName) {
            this.team = teamName;
            votes = new int[26];
        }

        public int compareTo(TeamVotes tv) {
            for (int i = 0; i < 26; i++) {
                if (this.votes[i] < tv.votes[i]) {
                    return 1;
                } else if (this.votes[i] > tv.votes[i]) {
                    return -1;
                }
            }
            return this.team - tv.team;
        }
    }
}
```

---
title: 642. Design Search Autocomplete System
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:42
---


Link: https://leetcode.cn/problems/design-search-autocomplete-system/

# Question

difficulty: high
adj diff: 5

    Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

    You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

    Here are the specific rules:

    The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
    If less than 3 hot sentences exist, return as many as you can.
    When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
    Implement the AutocompleteSystem class:

    AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
    List<String> input(char c) This indicates that the user typed the character c.
    Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
    Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

    Example 1:

    Input
    ["AutocompleteSystem", "input", "input", "input", "input"]
    [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    Output
    [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

    Explanation
    AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
    obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
    obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
    obj.input("a"); // return []. There are no sentences that have prefix "i a".
    obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

    Constraints:

    n == sentences.length
    n == times.length
    1 <= n <= 100
    1 <= sentences[i].length <= 100
    1 <= times[i] <= 50
    c is a lowercase English letter, a hash '#', or space ' '.
    Each tested sentence will be a sequence of characters c that end with the character '#'.
    Each tested sentence will have a length in the range [1, 200].
    The words in each input sentence are separated by single spaces.
    At most 5000 calls will be made to input.

# Code

用 Trie 结构。如下。

Someone else code：

```
    public class AutocompleteSystem {
    	class Node {
    		Node(String st, int t) {
    			sentence = st;
    			times = t;
    		}
    		String sentence;
    		int times;
    	}
    	class Trie {
    		int times;
    		Trie[] branches = new Trie[27];
    	}
    	public int int_(char c) {
    		return c == ' ' ? 26 : c - 'a';
    	}
    	public void insert(Trie t, String s, int times) {
    		for (int i = 0; i < s.length(); i++) {
    			if (t.branches[int_(s.charAt(i))] == null)
    				t.branches[int_(s.charAt(i))] = new Trie();
    			t = t.branches[int_(s.charAt(i))];
    		}
    		t.times += times;
    	}
    	public List < Node > lookup(Trie t, String s) {
    		List < Node > list = new ArrayList < > ();
    		for (int i = 0; i < s.length(); i++) {
    			if (t.branches[int_(s.charAt(i))] == null)
    				return new ArrayList < Node > ();
    			t = t.branches[int_(s.charAt(i))];
    		}
    		traverse(s, t, list);
    		return list;
    	}
    	public void traverse(String s, Trie t, List < Node > list) {
    		if (t.times > 0)
    			list.add(new Node(s, t.times));
    		for (char i = 'a'; i <= 'z'; i++) {
    			if (t.branches[i - 'a'] != null)
    				traverse(s + i, t.branches[i - 'a'], list);
    		}
    		if (t.branches[26] != null)
    			traverse(s + ' ', t.branches[26], list);
    	}
    	Trie root;
    	public AutocompleteSystem(String[] sentences, int[] times) {
    		root = new Trie();
    		for (int i = 0; i < sentences.length; i++) {
    			insert(root, sentences[i], times[i]);
    		}
    	}
    	String cur_sent = "";
    	public List < String > input(char c) {
    		List < String > res = new ArrayList < > ();
    		if (c == '#') {
    			insert(root, cur_sent, 1);
    			cur_sent = "";
    		} else {
    			cur_sent += c;
    			List < Node > list = lookup(root, cur_sent);
    			Collections.sort(list, (a, b) -> a.times == b.times ? a.sentence.compareTo(b.sentence) : b.times - a.times);
    			for (int i = 0; i < Math.min(3, list.size()); i++)
    				res.add(list.get(i).sentence);
    		}
    		return res;
    	}
    }

    /**
     * Your AutocompleteSystem object will be instantiated and called as such:
     * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
     * List<String> param_1 = obj.input(c);
     */
```

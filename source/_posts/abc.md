---
title: 1152. Analyze User Website Visit Pattern
comments: true
category: Leetcode
tags: []
---

Link: https://leetcode.cn/problems/analyze-user-website-visit-pattern/

# Question

difficulty: mid
adj diff: 3
    
    You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].
    
    A pattern is a list of three websites (not necessarily distinct).
    
        For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
    
    The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
    
        For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
        Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
        Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
    
    Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
    
    Example 1:
    
    Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
    Output: ["home","about","career"]
    Explanation: The tuples in this example are:
    ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
    The pattern ("home", "about", "career") has score 2 (joe and mary).
    The pattern ("home", "cart", "maps") has score 1 (james).
    The pattern ("home", "cart", "home") has score 1 (james).
    The pattern ("home", "maps", "home") has score 1 (james).
    The pattern ("cart", "maps", "home") has score 1 (james).
    The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
    
    Example 2:
    
    Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
    Output: ["a","b","a"]
    
     
    
    Constraints:
    
        3 <= username.length <= 50
        1 <= username[i].length <= 10
        timestamp.length == username.length
        1 <= timestamp[i] <= 109
        website.length == username.length
        1 <= website[i].length <= 10
        username[i] and website[i] consist of lowercase English letters.
        It is guaranteed that there is at least one user who visited at least three websites.
        All the tuples [username[i], timestamp[i], website[i]] are unique.

Java实现题，没什么高深莫测的算法。

# Code

以下代码来自于[leetcode上面的网友Hanxin](https://leetcode.cn/problems/analyze-user-website-visit-pattern/solution/cpython3java-1pai-xu-tong-ji-bao-li-zu-h-4q7j/)

1. 把 input 装入 一个struct，然后根据时间排序。
2. 统计每个用户，访问过的所有网站 eg. Joe -> {"baidu", "google", "gmail", "p站"}
3. 暴力方式，构建 3个word的pattern。
4. 注意：如果一个用户常访问同一个pattern，只算一次。（所以给每个用户一个新的 hashset）
5. 最终所有的pattern汇总到一个hashmap中，数一下max。

就没必要自己写代码了，以下是网友的代码。

```
class Node
{
    public String user;
    public int time;
    public String web;

    Node(String user_, int time_, String web_)
    {
        user = user_;
        time = time_;
        web = web_;
    }
}

class Solution 
{
    public List<String> mostVisitedPattern(String[] username, int[] timestamp, String[] website) 
    {
        int n = username.length;

        //----统计所有结点，按时间升序排序
        Node [] nodes = new Node [n];
        for (int i = 0; i < n; i ++)
        {
            nodes[i] = new Node(username[i], timestamp[i], website[i]);
        }
        Arrays.sort(nodes, new Comparator<>(){
            public int compare(Node a, Node b)
            {
                return a.time - b.time;
            }
        });

        //----统计每个用户，访问过的结点（已经是按时间升序）
        Map<String, List<Node>> user_visit = new HashMap<>();
        for (int i = 0; i < n; i ++)
        {
            Node x = nodes[i];
            user_visit.putIfAbsent(x.user, new ArrayList<>());
            user_visit.get(x.user).add(x);
        }

        //----每个用户，自己访问过的web，暴力构造长度为3的”路径“
        Map<String, Integer> path_freq = new HashMap<>();

        for (Map.Entry<String, List<Node>> entry : user_visit.entrySet())
        {
            String user = entry.getKey();
            List<Node> visit = entry.getValue();
            
            Set<String> tmp_path_uset = new HashSet<>();    //----防止一个路径重复访问（很容易WA）
            
            int nn = visit.size();
            for (int i = 0; i < nn; i ++)
            {
                for (int j = i + 1; j < nn; j ++)
                {
                    for (int k = j + 1; k < nn; k ++)
                    {
                        String cur_path = visit.get(i).web + "#" + visit.get(j).web + "#" + visit.get(k).web;
                        tmp_path_uset.add(cur_path);
                    }
                }
            }

            for (String path : tmp_path_uset)
                path_freq.put(path, path_freq.getOrDefault(path, 0) + 1);
                
        }

        int max_freq = 0;
        String res = "";
        for (Map.Entry<String, Integer> entry : path_freq.entrySet())
        {
            String path = entry.getKey();
            int f = entry.getValue();
            if (f > max_freq)
            {
                max_freq = f;
                res = path;
            }
            else if (f == max_freq)
            {
                String [] rr = res.split("#");
                String [] pp = path.split("#");
                if (pp[0].compareTo(rr[0]) < 0 || (pp[0].equals(rr[0])==true && pp[1].compareTo(rr[1]) < 0) || (pp[0].equals(rr[0])==true && pp[1].equals(rr[1])==true && pp[2].compareTo(rr[2]) < 0) )
                {
                    res = path;
                }
            }
        } 

        String [] tmp = res.split("#");
        List<String> ans = new ArrayList<>();
        for (String tm : tmp)
            ans.add(tm);
        return ans;
    }
}
```
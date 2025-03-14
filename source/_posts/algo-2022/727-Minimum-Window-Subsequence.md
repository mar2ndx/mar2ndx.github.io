---
title: 727. Minimum Window Subsequence
category: Leetcode
tags: []
comments: true
date: 2022-11-04 20:09
---



Link: https://leetcode.cn/problems/sliding-window-maximum/

# Question

difficulty: high
adj diff: 4

    Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

    If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

    

    Example 1:

    Input: s1 = "abcdebdde", s2 = "bde"
    Output: "bcde"
    Explanation: 
    "bcde" is the answer because it occurs before "bdde" which has the same length.
    "deb" is not a smaller window because the elements of s2 in the window must occur in order.

    Example 2:

    Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
    Output: ""

    

    Constraints:

        1 <= s1.length <= 2 * 104
        1 <= s2.length <= 100
        s1 and s2 consist of lowercase English letters.

注意：用Map来记录出现的 occurence count 是错误的解法！

因为，substring 的字母顺序不能变。

这是[网友给的正确的解法](https://leetcode.cn/problems/minimum-window-subsequence/solution/itcharge-727-zui-xiao-chuang-kou-zi-xu-l-v3az/)：

1. 向右扩大窗口，匹配字符，直到匹配完 s2 的最后一个字符。
1. 当满足条件时，缩小窗口，并更新最小窗口的起始位置和最短长度。
1. 缩小窗口到不满足条件为止。

> 这道题的难点在于第二步中如何缩小窗口。
>
> 当匹配到一个子序列时，可以采用逆向匹配的方式，从 s2 的最后一位字符匹配到 s2 的第一位字符。
> 找到符合要求的最大下标，即是窗口的左边界。

# Code

代码源自于：https://leetcode.cn/problems/minimum-window-subsequence/solution/shuang-zhi-zhen-jia-bi-100-by-tsinghuach-wf2z/

```
class Solution {
    public String minWindow(String s1, String s2) {
        //S = "abcdebdde", T = "bde"
        //left->    -<right
        //bcde   bde
        char [] s=s1.toCharArray();
        char [] t=s2.toCharArray();//转化的数组 
        int left=0;
        int right=0;
        int i=0;//循环t
        int start=0;//起始位置
        int minlength=s.length+1;//最短长度  //abcdebdde  a->e   a-d
        //abcdef  bcd
        while(left<s.length){ //遍历字符的起始位置
            if(s[left]==t[i]){
                i++;
            }
            if(i==t.length){//包含了
                right=left;//备份
                while(i>0){
                    if(s[left]==t[i-1]){ //相等，回退
                        i--;//退回，恢复0
                    }
                    left--;
                }
                left++;
                if(right-left+1<minlength){ //保存最短
                    minlength=right-left+1;//缩短长度
                    start=left;

                }
            }
            left++;
        }
        if(minlength==s.length+1){
            return "";
        }else{
            return s1.substring(start,start+minlength);
        }
    }
}
```

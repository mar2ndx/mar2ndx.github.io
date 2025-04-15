---
title: 【Tech】 Download all MP3 files in RSS feed
category: unknown
tags: technology
comments: true
date: 2022-03-01 00:00:00
---


# Why

For some reason, certain podcast are not accessible in China. Thus for good audio RSS content that I am afraid of missing out, downloading them and keep it offline is a nice idea. 

However, most RSS clients are not tailored for my use case, so instead of using any tools, I did some research and finally was able to download all MP3 from this podcast: 

1. (out of date) https://raw.githubusercontent.com/Reyshawn/FanpieFilmFeed/master/fanPieFilm.rss
1. (up to date)https://anchor.fm/fanpaifilm
1. (马后炮节目) https://rss.shawnxli.com/fanpie-film-ma
1. Latest: https://www.listennotes.com/zh-hans/podcasts/%E5%8F%8D%E6%B4%BE%E5%BD%B1%E8%AF%84%E8%80%B3%E6%97%81%E9%A3%8E-%E6%B3%A2%E7%B1%B3%E5%92%8C%E4%BB%96%E7%9A%84%E6%9C%8B%E5%8F%8B%E4%BB%AC-pRWES8tY-6H/

# 首次尝试

I did some research on [__podcatcher softwares__](https://en.wikipedia.org/wiki/List_of_podcast_clients), and no luck finding a good one. 

Failed. 

# 第二次尝试

Got some help from: 

https://www.commandlinefu.com/commands/view/14685/download-files-linked-in-a-rss-feed

And I used this command to exact all MP3 links:

    export HTTP_PROXY=http://127.0.0.1:58591; export HTTPS_PROXY=http://127.0.0.1:58591; export ALL_PROXY=socks5://127.0.0.1:51837

    curl -s https://raw.githubusercontent.com/Reyshawn/FanpieFilmFeed/master/fanPieFilm.rss | grep -o '<enclosure url="[^"]*' | grep -o '[^"]*$'

Here are the results: [Kaolafm content](/files/rss-kaola-links.txt)

Simply dump those links into IDM softwares and the rest are set. 

## 问题

I got a bunch of files with naming like these: 

```
82013211-c782-4a84-ad20-9001d1bdcd2e.mp3
4c6a181e-f8ff-4b9e-9c20-4a05e8edac84.mp3
```

No timestamp, no title, no good. 

# 第三次尝试

I found this blog super useful:

https://rakhesh.com/coding/downloading-all-episodes-of-a-podcast/

Thus I wrote the following __rss_script.sh__:

    for i in $(curl -s https://raw.githubusercontent.com/Reyshawn/FanpieFilmFeed/master/fanPieFilm.rss | grep -o '<enclosure url="[^"]*' | grep -o '[^"]*$'); do
        url=$i
        audiodir=$(echo $i | sed 's|http://image\.kaolafm\.net/mz/audios/||' | sed 's/\/.*\.mp3//')
        outfile=$(echo $i | sed 's|http://image\.kaolafm\.net/mz/audios/||')
        mkdir $audiodir
        wget -q $url -O $outfile
    done

Simply:

    bash rss_script.sh

and you shall have a nice time. Enjoy.

## 结果

All MP3s are in sub-folders like '201604' or '202112', however, I wasn't able to get the right title this time. 

# 第四次尝试

最终我发现，还是通过多项选择，表格，curl 的方法来弄比较好。

至于如何多行搜索选择，[可以看这里](/2022/04/20/Tech/technology/vscode-copy-all-search-results/)

这里拿 https://anchor.fm/s/4a4df770/podcast/rss 这个link 的下载过程，简单记录一下：

1. Extract title and mp3 links: [title](/files/rss-extracted-title.txt), [mp3](/files/rss-extracted-mp3.txt)
1. url 中有一些特殊字符需要处理：
	1. %2F 改为 /
	1. %3A 改为 :
	1. https:.*https 改为 https
1. Put them together in a csv file (maybe use Excel): [the csv file](/files/rss-title-mp3.csv)
1. Make a [curl bash](/files/rss-fanpai-main.sh) and another [example](/files/rss-fanpai-er.sh)
1. Execute the curl
1. Done

注意：在mac上，不要用 iTerm，而是用 Terminal，否则 copy special character 会出错。

# Reference

sed tutorial: https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux

Old content: [here](/files/RSS反派影评Feed.txt)

New content: [here](/files/RSS反派影评Feed-new.txt)

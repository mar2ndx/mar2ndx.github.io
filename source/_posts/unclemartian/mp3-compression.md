---
title: 【Tech】 MP3 compression
category: unknown
tags: technology
comments: true
date: 2022-04-26 00:00:00
---


# Tools

我使用了 Ubuntu 上的 lightweight audio tool：__Sound Converter__

	sudo apt-get install soundconverter

Config 方面，我尝试了 variable / low quality，感觉质量不错。

如下图。

![](/images/tech/mp3-compression-sound-converter.jpg)

# File Types

I tested out: 

1. MP3 format with dynamic average 54kbps with 32khz
1. AAC(m4a) format with fixed 64kbps with 44khz

两个文件大小差不多，m4a在大比率的情况下只比mp3大18%。

听上去效果是一样的。

所以最终选择了 mp3 格式。

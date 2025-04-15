---
title: 【Tech】 APT hold back a package from updating
category: unknown
tags: ubuntu
comments: true
date: 2022-05-09 00:00:00
---


# Why

According to this 热心网友的视频：[wps的linux版本目前还是11.1.0.10161好用
](https://www.bilibili.com/video/av935616825/)

> 最新版本功能还不全并且兼容也不及上一个版本好。
> 
> 当然还可以选择专业版的wps,不过专业版目前只能试用一个月，想要购买授权联系客服也未回应，所以还是推荐先用上一个版本。

so, I need a way to forbid WPS from updating. 

Btw, WPS is only available in:

    APT-Sources: https://apt.atzlinux.com/atzlinux buster/non-free

![](/images/tech/apt-mark-hold-back-version.png)

# Commands

查看信息：

    apt show wps-office
    apt list --upgradable

禁止 apt 更新：

    sudo apt-mark hold wps-office
    apt-mark showhold

然后就可以安全的：

    sudo apt update && sudo apt autoremove && sudo apt upgrade -y

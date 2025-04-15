---
title: 【Tech】 Gnome extension - Internet Radio
category: unknown
tags: ubuntu
comments: true
date: 2022-04-24 00:00:00
---


# Internet Radio

其实 Gnome 上不止一个 radio extension，但是没有一个是 work out-of-the-box on Pop!_OS. 

这是官网推荐的： [Listen to an Internet Radio Stream](https://extensions.gnome.org/extension/836/internet-radio/)

直接安装，出错。

## 安装报错

    Requiring GstPbutils, version none: Typelib file for namespace 'GstPbutils' (any version) not found

## Solution

根据[网友建议](https://github.com/hslbck/gnome-shell-extension-radio/issues/117): Installing __gir1.2-gst-plugins-base-1.0__ fixes the error. The internet radio now works.

所以安装依赖：

    sudo apt install gir1.2-gst-plugins-base-1.0

然后重新安装 internet-radio，最后重启 gnome。

Alt + F2，输入‘r’ ([This command mainly restarts the session without closing it.](https://ubunlog.com/en/restart-frozen-gnome-session/))

大功告成！

## Radio Catalog

https://www.radio-browser.info/search?page=1&order=clickcount&reverse=true&hidebroken=true&has_extended_info=true

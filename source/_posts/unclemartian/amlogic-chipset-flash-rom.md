---
title: 【Tech】 Amlogic 晶晨芯片刷机教程
category: unknown
tags: ubuntu
comments: true
date: 2021-11-03 09:00:00
---


# 前言

晶晨(Amlogic)芯片有很多种设备。我玩过4种(只有前两者刷Armbian成功)：

1. __Phicomm N1__（S905D / 2G）
1. __玩客云__（S805 / 1G）
1. CM201-1 魔百盒（S905L / 1G）
1. CM2000 红

其中每个设备都可以刷3种系统：

1. Android for TV
1. Armbian for Linux
1. Emuelec for gaming

# 结果

CM201-1 魔百盒这个机器，启动 Armbian 一直没问题，但是无论换什么 dtb，Armbian 都无法 boot。所以，就当电视盒子吧，还挺好用的。

> 这个帖子提到一个奇淫巧技，不知道能不能用，摘抄如下：
> 
> 使用adb shell reboot update发现启动失败，多次尝试也是如此。
> 
> 。。。受到启发，把启动盘根目录下的aml_autoscript.zip改名为update.zip,输入adb shell reboot update命令后直接引导进入armbian
> 
> https://blog.csdn.net/u012481946/article/details/113774089

CM2000 这个机器，不但无法刷 Armbian，连Android底包都坏了。重刷之后可以使用TV box 功能，但是无 Wifi，插线用。

wky是最容易刷的。我在其中一个上面装了 Armbian 跑同步盘，十分稳定。

N1有个问题，就是Android底包经常被弄坏（Armbian正常可启动）。只要重刷一下 Android 系统就好了。

> 为了刷n1，我弄坏了好几个u盘。而且好像最近买的这一批，只有32G可用于 Armbian，8G的一个都没成功。不知道为什么。

# N1刷机

## Android

对于 n1 盒子来说，使用这个Android底包就行：__斐讯盒子N1_YYFROM夏杰语音实用版__

http://www.yyfrom.com/cms/yyfrom/product/2021-7-3/166.html

刷机很简单。（需要去设备管理器种调整一下usb驱动，参考 https://post.smzdm.com/p/awkdzqvk/）

要注意2点：

1. Usb burning tool 软件中，先按“开始”，再连接 usb，否则 n1 连上直接就断开。
1. 一定要取消“擦除flash”和“擦除bootloader”。参考 https://post.smzdm.com/p/ax025099/

这个底包无法卸载 带广告的HDP。我用adb等进去，发现这个app装在 /system/app/ 里面了，不知道怎么卸载。算了。

![](/images/tech/usb-burning-tool-n1.jpg)

参考：https://post.smzdm.com/p/a25gpgx7/

## EmuElec

EmuELEC是专门为晶晨S905，S912以为更强的S922x/S905x2设计的系统。N1的高性价比加上周围随手可得的附件，成本基本可以控制在￥200左右，但却可以通过EmuELEC打造成一台拥有十几种机型几千个游戏的游戏平台，比国内很多人在安卓上使用老旧内核，效能极低，操控延迟很高的小鸡模拟器强大的多。

系统自带了多种游戏机，涵盖了Atari(雅达利) ，FC（NES任天堂），SNES（超级任天堂），N64(任天堂64)，GB，GBA，GBC（任天堂Gameboy家族），NDS（任天堂DS），PC Engine（NEC的家用游戏机），MD（世嘉Megadrive），DC（世嘉Dreamcast），PS(Sony Playstation)，PSP（Play Station Portable）以及各种复古街机版。游戏更是可以根据存储容量达到几千个。

得利于底层驱动的优化，在这么一台不到￥100的主机上，双倍渲染解析度玩PSP的《怪物猎人3HD》效果棒极了，比PSP本体玩效果都棒。

玩游戏玩腻了，通过系统中Advanced Options（增强选项）最下面的“返回安卓系统”则可以切换回N1盒子内部的安卓系统 。当然拔掉EmuELEC的系统U盘，重启盒子也可直接回到盒子内部的安卓系统。

安卓系统下各种视频播放软件比如优酷，爱艺奇以及B站在2G Ram的4核ARM Cortex-A53 1.5GHz处理器下运行毫无压力，加载以及播放速度也在5G或者千兆有线的加持下非常迅速。装一个Kodi观看NAS或者移动硬盘中的4K蓝光原盘的效果棒极了。

除了N1，你还可以选择魔巧盒Q5。除了配置和颜值比N1低了一些，装EmuELEC的话差别不大，只是因为是1G ram，当安卓电视盒子的话反而有些不太给力。

> Emuelec(xxxELEC之类的系统)与Armbian不兼容，启动过ELEC就启动不了Armbian了，反之可以。
>
> 所以ELEC对boot环境具有破坏性，只能想办法恢复原来的boot环境，重新刷机可以解决。

刷机过程，参考这里：

https://www.cnblogs.com/milton/p/11883811.html

### 什么是 CoreELEC？

CoreELEC is a ‘Just enough OS’ Linux distribution based on Kodi1 technology for popular Amlogic hardware

CoreELEC是一个小巧的Linux发行版系统，从LibreELEC分离出来，是专为Amlogic（晶晨）芯片开发的Linux与Kodi集成的媒体中心系统。它的界面就是Kodi的界面，可以独立运行于U盘或TF卡。可最大限度的利用硬件资源，流畅的播放视频，100G的4K视频在低配设备上也能顺利播放。另外CoreELEC可以完美输出杜比全景声和dtsx，低端的安卓则不行。各种音频完美直通，无论是ac3、dts还是次世代音轨truehd、dtshd，包括atmos、dts-x等各种音轨都可以完美直通到功放解码。

Coreelec是专门面向Amlogic芯片设备适配的，推荐s905、s912、s922系列的盒子安装使用，例如：斐讯N1、章鱼星球。

## Armbian

Armbian 经常把 Android系统搞坏。哎。

另外，试用了桌面版的 Debian 9，实在是没什么可用性，而且有时候无法自动连接 Wifi。不建议玩儿。

最佳的固件就是 5.77版本的 Debian stretch。

5.99 / 20.10 版本我没成功过。

# WKY刷机

参见另一篇《Debian 9 (Armbian) on N1/Wky 使用教程》

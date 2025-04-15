---
title: 【Tech】 Mint Linux - remove Xfce and install Cinnamon
category: unknown
tags: ubuntu
comments: true
date: 2022-04-27 00:00:00
---


# Install Cinnamon

    sudo apt install cinnamon
    sudo apt install cinnamon-desktop-environment lightdm

（这里，lightdm 安装之后好像不需要配置）

登录的时候，可以选一下桌面环境：

1. Xfce
2. Cinnamon
3. Cinnamon with Software Rendering

选第二项。

# Remove Xfce

    sudo apt remove xfce*
    dpkg -l | grep .xfce. 
    dpkg -l | grep .xfce. | xargs sudo apt-get remove
    sudo dpkg -l | grep .xfce. | xargs sudo apt-get remove

# Reference

https://www.ubuntubuzz.com/2019/05/how-to-completely-remove-xfce-desktop-from-mint-xfce-191.html

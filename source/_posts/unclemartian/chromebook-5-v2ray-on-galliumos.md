---
title: 【Tech】 Chromebook Tutorial 5 - v2ray on GalliumOS
category: unknown
tags: ubuntu
comments: true
date: 2022-04-16 00:00:00
---


# Overview 

In this post, we'll try to install Qv2ray and v2rayLui on __[GalliumOS 3.1](https://wiki.galliumos.org/Welcome_to_the_GalliumOS_Wiki)__.

None of those succeeded.

# Qv2ray

The installation of AppImage + v2core is straight-forward. Just make sure to download the right version: 

1. Qv2ray 2.7 : https://github.com/Qv2ray/Qv2ray/releases
1. v2ray as vcore in the config folder. 
1. config group as a subscription.

## 运行

出现 error：

    (process:15945): dconf-WARNING **: 13:15:33.425: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15949): dconf-WARNING **: 13:15:33.450: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1
    [SystemProxy] [0] Program: gsettings, Args: set;org.gnome.system.proxy;mode;manual [SystemProxy] [0] Program: gsettings, Args: set;org.gnome.system.proxy.http;host;127.0.0.1 [gRPCBackend] gRPC Version: 1.19.1 
    [gRPCBackend] API call returns: 14 (Connect Failed) 
    [gRPCBackend] API call returns: 14 (channel is in state TRANSIENT_FAILURE) 
    [gRPCBackend] API call returns: 14 (channel is in state TRANSIENT_FAILURE) 
    [gRPCBackend] API call returns: 14 (channel is in state TRANSIENT_FAILURE) 
    [gRPCBackend] API call returns: 14 (channel is in state TRANSIENT_FAILURE) 
    [gRPCBackend] API call returns: 14 (channel is in state TRANSIENT_FAILURE) 

    (process:15953): dconf-WARNING **: 13:15:33.495: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15960): dconf-WARNING **: 13:15:33.512: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15964): dconf-WARNING **: 13:15:33.532: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15968): dconf-WARNING **: 13:15:33.553: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15973): dconf-WARNING **: 13:15:33.575: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1

    (process:15977): dconf-WARNING **: 13:15:33.603: failed to commit changes to dconf: Error spawning command line “dbus-launch --autolaunch=896b12ea52f87d428e7dd579ae1b587e --binary-syntax --close-stderr”: Child process exited with code 1


经过反复的测试，GalliumOS上的 Qv2ray 用不了。

不知原因。

# v2rayLui

先安装 铜豌豆。

然后：

    sudo apt install v2raylui
    sudo apt install v2ray 

这时候会遇到的问题是：v2ray : PreDepends: init-system-helpers (>= 1.54~) but 1.51 is to be install

解决办法：

    wget http://launchpadlibrarian.net/173841617/init-system-helpers_1.54_all.deb

或者

    wget http://ports.ubuntu.com/pool/main/i/init-system-helpers/init-system-helpers_1.57_all.deb

方便起见，我直接放这里了：

    wget https://mar2ndx.github.io/files/init-system-helpers_1.18_all.deb

    wget https://mar2ndx.github.io/files/init-system-helpers_1.57_all.deb

## 查看 apt 包的历史版本

这样做：

    apt-cache policy v2ray

## 运行

    v2raylui

结果：

    [15675] Error loading Python lib '/tmp/_MEILnaXkU/libpython3.7m.so.1.0': dlopen: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found (required by /tmp/_MEILnaXkU/libpython3.7m.so.1.0)

估计是默认的 python3 版本问题。

# 总结

GalliumOS 3.1 翻不了墙。

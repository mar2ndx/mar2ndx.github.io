---
title: 【Tech】 Ubuntu System Commands
category: unknown
tags: ubuntu
comments: true
date: 2021-08-13 00:00:00
---


# System commands

## Check version of Ubuntu

    lsb_release -a
    cat /etc/issue
    cat /etc/os-release
    hostnamectl

## Ubuntu switch to Aliyun source

    ls /etc/apt/
    sudo cp -ra /etc/apt/sources.list /etc/apt/sources.list.backup

Next check current system's codename: 

    lsb_release -a

把’TODO’的地方换成上面的Codename

    deb http://mirrors.aliyun.com/ubuntu/ TODO main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ TODO main restricted universe multiverse

    deb http://mirrors.aliyun.com/ubuntu/ TODO-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ TODO-security main restricted universe multiverse

    deb http://mirrors.aliyun.com/ubuntu/ TODO-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ TODO-updates main restricted universe multiverse

    deb http://mirrors.aliyun.com/ubuntu/ TODO-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ TODO-proposed main restricted universe multiverse

    deb http://mirrors.aliyun.com/ubuntu/ TODO-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ TODO-backports main restricted universe multiverse

Alternatively, 也可以用 163网易源（下面以 Ubuntu 20.04 focal 为例）：

    deb http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
    deb http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse
    # deb-src http://mirrors.163.com/ubuntu/ focal main restricted universe multiverse
    # deb-src http://mirrors.163.com/ubuntu/ focal-security main restricted universe multiverse
    # deb-src http://mirrors.163.com/ubuntu/ focal-updates main restricted universe multiverse
    # deb-src http://mirrors.163.com/ubuntu/ focal-backports main restricted universe multiverse

下面以 Debian GNU/Linux 11 (bullseye) 为例: 

deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib

deb https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main

deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib

deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib

参考：https://www.cnblogs.com/liuguanglin/p/debian11_repo.html

Done, after this do: sudo apt-get update and upgrade.

## Ubuntu 安装中文输入法

Uninstall ibus first, then install fcitx: 

    sudo apt-get purge ibus
    sudo apt-get autoremove
    sudo apt-get install fcitx

Then go to system language config, install Chinese and apply system-wide.

Change input from ibus to fcitx. Reboot system. 
Then run:

    sudo dpkg -i sogoupinyin_2.4.0.3469_amd64.deb
    sudo apt -f install


### 默认输入法 切换简繁体字

Use "Ctrl + Shift + F"

## 设置 alias 短命令

    alias new_name='old command'

要创建永久别名，您必须.bashrc在主目录中编辑文件。

## 系统无法读写

Encounter "Missing write access to /usr/local/lib/node_modules"

Run the following: 

    sudo chown -R $USER /usr/local

Reference：https://teamtreehouse.com/community/getting-error-missing-write-access-to-usrlocallibnodemodules

## Ubuntu16.04挂载exfat格式U盘

    sudo apt-get install exfat-fuse

## Check disk usage

    df -h | grep -v '/snap\|tmp'

The -v inverses the grep search

The \| 实现grep OR的操作

Example output:

    Filesystem       Size  Used Avail Use% Mounted on
    udev             3.8G     0  3.8G   0% /dev
    /dev/nvme0n1p8    26G  5.1G   20G  21% /
    /dev/nvme0n1p9    35G  6.3G   27G  20% /usr
    /dev/nvme0n1p7   343M  139M  178M  44% /boot
    /dev/nvme0n1p10   54G  4.0G   47G   8% /home

# Software commands

## Install software using Snap

Snap is the command-line version of "Ubuntu Software", but the latter is very slow.

    snap search figma-linux
    snap install figma-linux 
    snap list
    snap info figma-linux

## Install XMind 8 on Ubuntu 20

新版本的XMind太多广告了，所以我安装了老版本的XMind 8 (R3.7.9 released in 2019)。

1. 解压缩 “xmind-8-update9-linux.zip” 到桌面。

1. 创建 XMind8.desktop 以下内容：

    [Desktop Entry]
    Name=XMind8
    Exec=/home/michael/Desktop/xmind-8-update9-linux/XMind_amd64/XMind
    Path=/home/michael/Desktop/xmind-8-update9-linux/XMind_amd64
    Terminal=false
    Type=Application
    Icon=xmind
    Comment=Xmind8
    Categories=Utility;

1. 一定注意，Path= 这个地方很重要，否则xmind将会无法找到 config。

    Refer to https://bbs.deepin.org/post/174888

1. 然后，右键点击这个 icon，选择 allow launching。
就可以啦～ 

1. optionally，可以把这个 icon 复制到系统 applications 文件夹，如下：

    sudo cp xmind-8.desktop /usr/share/applications/

## Install screen recorder

    sudo apt install python3-cairo python3-xlib kazam

## Install video player

    sudo apt-get install vlc -y

## Install Brackets

    sudo snap install brackets --classic

## Install Chrome

Use the deb file. 

Remove Chromium since it's not possible to sync with Google any more. 

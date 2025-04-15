---
title: 【Tech】 Install Wechat on Ubuntu
category: unknown
tags: ubuntu
comments: true
date: 2021-09-12 00:00:00
---


# ubuntu-deepin-wechat

Installer for Deepin WeChat with Wine

## Install Dependencies

```bash
cd deepin-wine-dependency
bash install.sh
```

## Install WeChat

```bash
sudo dpkg -i deepin.com.wechat_2.6.2.31deepin0_i386.deb
sudo apt-get install -f
```

## WeChat Version Too Old Issue

Please update your WeChat Windows installer if you encounter this problem.

```bash
mkdir /tmp/wechat
cd /tmp/wechat
wget https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe
env WINEPREFIX=/home/${USER}/.deepinwine/Deepin-WeChat deepin-wine WeChatSetup.exe
```

## WeChat font issue

Download:
https://github.com/qiuhuachuan/fonts/blob/main/MSYH.TTC

```bash
cp ~/Downloads/msyh.ttc ~/.deepinwine/Deepin-WeChat/drive_c/windows/Fonts
vim ~/.deepinwine/Deepin-WeChat/font.reg
```

File content: 

```bash
REGEDIT4
[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontSubstitutes]
"MS Shell Dlg"="msyh"
"MS Shell Dlg 2"="msyh"

[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontLink\SystemLink]
"Lucida Sans Unicode"="msyh.ttc"
"Microsoft Sans Serif"="msyh.ttc"
"MS Sans Serif"="msyh.ttc"
"Tahoma"="msyh.ttc"
"Tahoma Bold"="msyhbd.ttc"
"msyh"="msyh.ttc"
"Arial"="msyh.ttc"
"Arial Black"="msyh.ttc"
```

Last: 

```bash
WINEPREFIX=~/.deepinwine/Deepin-WeChat/ deepin-wine regedit ~/.deepinwine/Deepin-WeChat/font.reg
```

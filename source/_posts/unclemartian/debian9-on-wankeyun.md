---
title: 【Tech】 Debian 9 (Armbian) on N1/Wky 使用教程
category: unknown
tags: ubuntu
comments: true
date: 2021-10-15 00:00:00
---


这里使用 N1 和 玩客云（简称wky）。

# Debian 9

以 玩客云 硬件为例，测试使用 ARMBIAN 5.88 / Debian 9.9 版的 Armbian 系统。

硬件信息如下：

     ____   ___   ___  ____
    / ___| ( _ ) / _ \| ___|
    \___ \ / _ \| | | |___ \
     ___) | (_) | |_| |___) |
    |____/ \___/ \___/|____/

    Welcome to ARMBIAN 5.88 user-built Debian GNU/Linux 9 (stretch) Mr-Li,QQ:691048250
    System load:   0.70 0.52 0.26  	Up time:       7 min
    Memory usage:  8 % of 996MB  	IP:            192.168.31.33
    Usage of /:    25% of 6.4G

Debian 9.9 （stretch）

    root@aml:~# lsb_release -a
    No LSB modules are available.
    Distributor ID:	Debian
    Description:	Debian GNU/Linux 9.9 (stretch)
    Release:	9.9
    Codename:	stretch

而N1，则是使用 ARMBIAN 5.77 / Debian 9.8 版的固件:

	 ____  ___   ___  ____  
	/ ___|/ _ \ / _ \| ___| 
	\___ \ (_) | | | |___ \ 
	 ___) \__, | |_| |___) |
	|____/  /_/ \___/|____/ 
							

	Welcome to ARMBIAN 5.77 user-built Debian GNU/Linux 9 (stretch) 5.0.2-aml-s905   
	System load:   2.21 2.80 2.86   Up time:       6:33 hours               
	Memory usage:  30 % of 1838MB   Zram usage:    26 % of 919Mb    IP:            169.254.10.11 192.168.123.242
	CPU temp:      50°C             
	Usage of /:    11% of 29G       storage/:      44% of 128M 

更新至最新版 stretch：

	arm@armbian-n1-white-32g:~$ lsb_release -a
	No LSB modules are available.
	Distributor ID: Debian
	Description:    Debian GNU/Linux 9.13 (stretch)
	Release:        9.13
	Codename:       stretch

## Armbian installation

### on WKY

只要是将U盘烧好了“Armbian_5.88内置emmc需要U盘刷” 固件（1.5GB img file）。

然后插上wky，自动重装系统装如EMMC（不用刷inphic底包），很方便。

WKY可能不支持卡载 armbian？

### on N1

N1是支持卡在armbian的，但是我用了几个小时，搞坏了一个20块钱的U盘，故无法确定卡载系统的稳定性。

刷机很简单，将这两个固件任选其一：

1. Armbian_5.77_Aml-s905_Debian_stretch_default_5.0.2_20190401.img
1. Armbian_5.77_Aml-s905_Debian_stretch_default_5.0.2_desktop_20190401.img

用 balenaEtcher 写入U盘，然后改一下 uEnv.ini 就行了。

如果无法启动，通过 Reboot to Elec apk来引导一下就行。

## 首次启动

默认密码 default：

root/1234

## Check 32 bit or 64 bit

    getconf LONG_BIT

## 修改系统时区

    armbian-config

#选择Personal
#选择Timezone
#选择Asia
#选择Shanghai
#然后依次选择 back exit 退出。

## hostname

Check / Change:

    hostname
    sudo hostname armbian-wky

## 换源

    cd /etc/apt/
    vi sources.list

### For Debian 9 stretch

Note that Tsinghua and 163.com sources DO NOT WORK.

    deb https://mirrors.ustc.edu.cn/debian/ stretch main contrib non-free
    deb-src https://mirrors.ustc.edu.cn/debian/ stretch main contrib non-free

    deb https://mirrors.ustc.edu.cn/debian/ stretch-updates main contrib non-free
    deb-src https://mirrors.ustc.edu.cn/debian/ stretch-updates main contrib non-free

    deb https://mirrors.ustc.edu.cn/debian/ stretch-backports main contrib non-free
    deb-src https://mirrors.ustc.edu.cn/debian/ stretch-backports main contrib non-free

    deb https://mirrors.ustc.edu.cn/debian-security/ stretch/updates main contrib non-free
    deb-src https://mirrors.ustc.edu.cn/debian-security/ stretch/updates main contrib non-free

如果签名报错，运行这一行：

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 公钥（例如648ACFD622F3D138）

就好了。

For docker

    https://mirrors.ustc.edu.cn/docker-ce

### For Ubuntu 18 bionic

这个比较难搞，arm 版本的源不好找。

不是 “Failed to fetch” 就是 certificate 有问题。

亲测以下可用:

	# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
	deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic main restricted universe multiverse
	deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-updates main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-updates main restricted universe multiverse
	deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-backports main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-backports main restricted universe multiverse
	deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-security main restricted universe multiverse
	# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-security main restricted universe multiverse

或者：

	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial main
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial main

	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial-updates main
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial-updates main

	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial universe
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial universe
	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial-updates universe
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial-updates universe

	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial-security main
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial-security main
	deb http://mirrors.aliyun.com/ubuntu-ports/ xenial-security universe
	deb-src http://mirrors.aliyun.com/ubuntu-ports/ xenial-security universe

Reference: https://www.bianchengquan.com/article/453596.html
和 https://www.jianshu.com/p/fd3a2d153505

## Some useful apt to install 

    apt install python-setuptools
    apt install tmux
    apt install mosh

## Install Webmin

国外版的宝塔。

    /etc/apt/sources.list.d/
    vi webmin.list

内容：

    deb http://download.webmin.com/download/repository sarge contrib

然后：

    wget http://www.webmin.com/jcameron-key.asc --no-check-certificate
    apt-key add jcameron-key.asc
    apt update
    apt install webmin

然后就可以在 10000 端口查看 webmin 面板了。

# 自动同步 + 挂在U盘

## 挂载 U盘

TODO

一定不要修改 fstab。教训。

## 同步软件

1. resilio sync
1. syncthing

### Resilio-sync

    apt install resilio-sync
    systemctl status resilio
    systemctl start resilio-sync
    systemctl status resilio-sync
    systemctl enable resilio-sync

查看：

https://192.168.123.215:8888/gui/

### Syncthing

    sudo apt install syncthing
    syncthing --version 

For Debian:

    cd /lib/systemd/system/

For Ubuntu:

    cd /etc/systemd/system/

Note the following config is ready:

    cat syncthing@.service
    sudo systemctl enable syncthing@$USER

After this, __/etc/systemd/system/multi-user.target.wants/syncthing@root.service__ is created. 

Run syncthing:

    sudo systemctl start syncthing@$USER
    sudo systemctl status syncthing@$USER
    vi /root/.config/syncthing/config.xml
    
将 <address>127.0.0.1:8384</address> 改成 0.0.0.0:8384

tls=“false” 改成 true

然后：

    sudo systemctl restart syncthing@$USER
    sudo systemctl status syncthing@$USER

查看：

https://192.168.123.215:8384

# 系统配置

## 桌面环境

Debian可以有桌面系统。

### 配置远程登陆

	sudo apt install xrdp xorgxrdp
	sudo systemctl enable xrdp
	sudo reboot

然后就可以用windows remote 软件来登陆了。Mac也可以。

端口号3389。

### 桌面自动登陆

	sudo vi /etc/lightdm/lightdm.conf

Remove the # and change it to have your username after (for example: autologin-user=test).

## 中文支持

	sudo apt-get install ttf-wqy-zenhei
	sudo vi /etc/locale.gen

去掉zh_CN.UTF-8前面的# 保存

	fc-cache -v
	sudo vi /etc/default/locale 

在 LANG=en_US.UTF-8 后面增加 LC_CTYPE=zh_CN.UTF-8

## 自动化 Hexo

	sudo vi /root/.bashrc
	source /root/.bashrc 

Add

	alias wiki="cd /home/rslsync/Resilio\ Sync/yellowpage/mar2ndx && git status && git add . && git commit -m 'auto hexo post update' && git push origin hexo-source && git status"

下次，只需要执行一行就行了：

	wiki

## Samba

	apt-get install samba
	systemctl status smbd
	(maybe optional)smbpasswd -a smb

然后

	sudo vi /etc/samba/smb.conf

	[wky]
		comment = wky-arm
		path = /home/rslsync/Resilio Sync/
		comment = share all
		browseable = yes
		public = yes
		writable = yes
		valid users = wky
		force user = wky
		force group = wky

重启：

	systemctl restart smbd
	systemctl status smbd

权限有问题。

# Reference

https://leeyr.com/323.html
https://www.znds.com/tv-1197649-1-1.html
https://post.smzdm.com/p/alpwnxmp/
https://blog.ztluo.dev/post/0057-phicomm-n1/

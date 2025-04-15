---
title: 【Tech】 Pop!_OS install Sunloginclient
category: unknown
tags: ubuntu
comments: true
date: 2022-04-17 00:00:00
---


# Overview

向日葵默认只支持 Ubuntu，或者 Ubuntu 衍生的系统，例如 Mint(?)。所以 __postinstall script 会报错__，连删除都困难。

另外，Pop!_OS 默认用 GDM 而不是 LightDM。

## 解决办法 x2

1. Temporarily change my OS informaiton to __Ubuntu 20.04 LTS__ while installing sunloginclient.
1. Extract the deb, __modify the common.sh script__, and repack the deb. 

当然也可以借鉴 [linux mint19.3（Debian）完美安装向日葵
](https://blog.csdn.net/ieeso/article/details/110916659) 的思路，直接改脚本。I did not have too much luck trying that （主要是嫌麻烦）. 

# Soluiton 1

## 直接安装 deb 报错

	Error:unknown OS it not impl
	Installation failed
	dpkg: error processing package sunloginclient (–install):
	installed sunloginclient package post-installation script subprocess returned error exit status 1

原因：向日葵只支持 Ubuntu，Deepin 和 麒麟系统。估计是给掏钱了。其他即使是 Ubuntu 或者 Debian-based OS 都故意无获得支持。[摘抄代码如下](https://forums.debiancn.org/t/topic/2801/5)：

	if [ $os_name == 'ubuntu' ] || [ $os_name == 'deepin' ] || [ $os_name == 'kylin' ]; then
	        echo $os_name > /dev/null 2>&1
	else
	        echoAndExit 'unknown OS it not impl'
	fi

## postinst/postrm scripts

现在做脚本分析。

向日葵的 scripts 在以下几个地方：

	sentry@pop-os:~$ ls /var/lib/dpkg/info/sunloginclient.
	sunloginclient.list      sunloginclient.postinst  sunloginclient.preinst
	sunloginclient.md5sums   sunloginclient.postrm    sunloginclient.prerm

还有

	sentry@pop-os:~$ ls /usr/local/sunlogin/scripts/
	checksun.sh                runsunloginclient.conf
	common.sh                  runsunloginclient.service
	depends.sh                 start.sh
	host                       stop.sh
	init_runsunloginclient     sunhost.sh
	lightdm.conf               uninstall.sh

1. 安装时的报错源于 /var/lib/dpkg/info/sunloginclient.postinst
1. 移除时的报错源于 /var/lib/dpkg/info/sunloginclient.postrm

但其实，这些 scripts 里面的 __$os_name__ 值其实来自于 __/usr/local/sunlogin/scripts/common.sh__

下面是解决过程。方法源自：[如何在linux mint20系统上安装向日葵远程软件
](https://blog.csdn.net/panxl6/article/details/108032700)，以及[ubuntu 发行版安装向日葵远程控制软件](https://www.codeleading.com/article/54725962164/).

## 暂时更改系统信息

	sudo mv /etc/os-release /etc/os-release.backup
	sudo mv /etc/issue /etc/issue.backup
	sudo vi /etc/issue

写入：

	Ubuntu 20.04 LTS \n \l

保存并退出。

All should be good. 暂时不用管 __os-release 文件缺失__。

现在，重新安装。

	sudo apt remove sunloginclient
	sudo dpkg -i sunloginclient-11.0.0.36662-amd64.deb

## dpkg 无法删除

报错：

	The package needs to be reinstalled, but I can’t find an archive for it

如果无法删除旧的 installation，那说明 dpkg 

	ls /etc/systemd/system/multi-user.target.wants/
	cd /var/lib/dpkg/
	sudo cp status status.backup
	sudo vi status

就可以删除了。

## GDM 报错

	... no /etc/gdm/Init/Default file

这个原因是，

[需要另一个桌面显示管理器](https://ask.csdn.net/questions/7503981)： 

	sudo apt install lightdm

如果跳出 config lightdm 的话，不用管，继续使用 gdm3 就好。

![](/images/tech/install-sunloginclient-lightdm.png)

之后 GUI 就正常运行了。

## OS 信息恢复

	sudo mv /etc/issue /etc/issue.Ubuntu20.04
	sudo mv /etc/issue.backup /etc/issue
	sudo mv /etc/os-release.backup /etc/os-release

结束，撒花。

# Soluiton 2

> [亲测有效](https://ask.csdn.net/questions/7503981) 修改deb方法参考 https://blog.csdn.net/yygydjkthh/article/details/36695243
>
> 解压后 修改 /解压文件夹/usr/local/sunlogin/scripts 里 common.sh 第78行 
>
> 将os_name=$(get_os_name) 改为 os_name=ubuntu

根据[这个回复](https://forums.debiancn.org/t/topic/2801/5)，可以看到并不复杂：

1. 下载 .deb 软件包

1. 执行命令 

		dpkg-deb -R ./sunloginclient-11.0.0.36662-amd64.deb sunloginclient

1. 进入 sunloginclient 文件夹，编辑软件包内容
回到软件包所在目录，执行命令

		dpkg-deb -b sunloginclient sunloginclient-11.0.0.36662-fixed-amd64.deb

1. 执行命令 

		sudo apt ./sunloginclient-11.0.0.36662-fixed-amd64.deb

以上就OK了。

我没试。

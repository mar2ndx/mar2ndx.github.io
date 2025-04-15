---
title: 【Tech】 Install OpenMediaVault on Debian
category: unknown
tags: ubuntu
comments: true
date: 2021-10-19 13:00:00
---


# OpenMediaVault

我安装失败了。

进了 登陆页面，然后无法登陆，我也不知道为什么。把 commands 记录在这里，没时间继续弄了。

Add the package repositories:

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb https://packages.openmediavault.org/public arrakis main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis main
    ## Uncomment the following line to add software from the proposed repository.
    # deb https://packages.openmediavault.org/public arrakis-proposed main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb https://packages.openmediavault.org/public arrakis partner
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis partner
    EOF

Install the openmediavault 4 (Arrakis) package:

    export LANG=C
    export DEBIAN_FRONTEND=noninteractive
    export APT_LISTCHANGES_FRONTEND=none
    
    wget -O "/etc/apt/trusted.gpg.d/openmediavault-archive-keyring.asc" https://packages.openmediavault.org/public/archive.key
    apt-key add "/etc/apt/trusted.gpg.d/openmediavault-archive-keyring.asc"
    
    apt-get update
    apt-get --allow-unauthenticated install openmediavault-keyring
    
    apt-get update
    apt-get --yes --auto-remove --show-upgraded \
        --allow-downgrades --allow-change-held-packages \
        --no-install-recommends \
        --option Dpkg::Options::="--force-confdef" \
        --option DPkg::Options::="--force-confold" \
        install postfix openmediavault

如果到这，安装不成功，往下看。

更新omv源

    echo "deb Index of /public arrakis main" > /etc/apt/sources.list.d/openmediavault.list

下载添加key

    apt-key adv --recv-keys --keyserver OpenPGP Keyserver 7E7A6C592EF35D13 24863F0C716B980B

语言包及环境变量等设置

    export LANG=C

    export DEBIAN_FRONTEND=noninteractive

    export APT_LISTCHANGES_FRONTEND=none

安装omv

    apt update

    apt install openmediavault-keyring postfix

    apt install openmediavault

    If not working: 

    apt --option Dpkg::Options::="--force-confdef" --option DPkg::Options::="--force-confold" install openmediavault

You will get the following screen: 

    Complete the installation                                                                                                                                                │
        │                                                                                                                                                                          │
        │ To complete the installation you need to run the following command:                                                                                                      │
        │                                                                                                                                                                          │
        │  omv-initsystem                                                                                                                                                          │
        │                                                                                                                                                                          │
        │                                                                                                                                                                          │
        │ To manage the system visit the openmediavault web control panel via a web browser:                                                                                       │
        │                                                                                                                                                                          │
        │  http://<IP or hostname>                                                                                                                                                 │
        │                                                                                                                                                                          │
        │                                                                                                                                                                          │
        │ By default the web control panel administrator account has the username 'admin' and password 'openmediavault'. It is recommended that you change the password for this   │
        │ account within the web control panel or using the 'omv-firstaid' CLI command.                                                                                            │
        │

    
基本成功了。然后我在跑：

    omv-initsystem

的时候，报错了。

我用 IP 地址尝试登陆一下，load 界面没问题，但是无法登陆。

# Reference

https://openmediavault.readthedocs.io/en/4.x/installation/on_debian.html

https://zhuanlan.zhihu.com/p/345143096


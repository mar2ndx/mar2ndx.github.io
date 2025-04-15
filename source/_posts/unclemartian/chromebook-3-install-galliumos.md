---
title: 【Tech】 Chromebook Tutorial 3 - Install GalliumOS
category: unknown
tags: ubuntu
comments: true
date: 2022-03-28 00:00:00
---


# Overview

There are 2 ways to do a fresh installation of GalliumOS on Chromebook:

1. __Traditional Mode__ - replace ChromeOS entirely. Need a USD drive. 
1. __chrx Mode__ - install from ChromeOS command line. 

The master guide is on __[wiki.galliumos.org](https://wiki.galliumos.org/Installing)__, or there's another [simpler guide for beginners](https://wiki.galliumos.org/Installing/New_To_Linux).

# 一、Traditional installtion 

1. Go to __[chrome://system](chrome://system)__, and look for __hardware_class__. For my case it says "Akali" and "C5B-A4B-xxxxxxxx"

    ![](/images/tech/galliumos-install-1.jpg)

1. Go to https://wiki.galliumos.org/Hardware_Compatibility and check against your hardware class. I got __"Intel Kaby Lake"__.

1. Go to https://galliumos.org/download and download ISO of your version. 

1. Enabling Developer Mode (Esc+F3(refresh)+Power), and reboot.

1. Enable Legacy Mode booting.

    1. With your ChromeOS booted, press [Ctrl+Alt+T] and get a terminal ("crosh") window
    1. Run: __'shell'__
    1. Then:

        sudo crossystem dev_boot_legacy=1

    1. If you have seen an error, simply skip and continue. (Reference: https://www.reddit.com/r/chrultrabook/comments/o9538s/trying_to_boot_from_usb_what_is_dev_boot_altfw_as/)

1. Disable WP (write protection). Check your device on [this MrChromebox](https://mrchromebox.tech/#devices) page to decide how you going to do it. In my case I use [the CR50 method](https://wiki.mrchromebox.tech/Firmware_Write_Protect#Hardware_Write_Protection)
    
    * If you still not sure, check out this video: https://www.youtube.com/watch?v=EGZ6KfjEPP0

1. Check WP status, At __crosh>__

        sudo sh
        flashrom --wp-status

    ![](/images/tech/galliumos-install-2.jpg)

1. Update Firmware. Press __[Ctrl+Alt+T]__ to get a terminal ("crosh") window, then type in "__shell__"
    * Decide if you wish to [update RW_LEGACY or install Full Firmware/UEFI](https://wiki.galliumos.org/Firmware)
    * Run: 

            cd; curl -LO https://mrchromebox.tech/firmware-util.sh && sudo bash firmware-util.sh

        In case Github not accissible, try this link: 

            cd; curl -LO https://mar2ndx.github.io/files/mrchromebox/firmware-util.sh && sudo bash firmware-util.sh

1. At promp, first you need to set GBB Flags (here is [an explanation of why](https://mrchromebox.tech/#fwscript)).

    > [Important: If you choose an ISO install of GalliumOS](https://wiki.galliumos.org/Installing) (thus removing ChromeOS), and choose to use the Legacy Boot Mode of the stock firmware (ie, with the stock or updated RW_LEGACY firmware), and __[you allow your battery to drain completely](https://wiki.galliumos.org/Firmware#crossystem)__, you might have a problem booting GalliumOS. This is due to the Developer Mode boot flag enabling Legacy Boot mode being reset when power is lost - see crossystem flags.
    >
    > Google Binary Block (GBB) flags are firmware level settings stored directly in the firmware flash chip itself in a read-only (RO) area
    >
    > I've made this mistake before. Had to do an entire factory restore of ChromeOS.

1. To set GBB, under ChromeOS at chronos@localhost / $ prompt, run this: 

        cd; curl -LO mrchromebox.tech/firmware-util.sh
        sudo install -Dt /usr/local/bin -m 755 firmware-util.sh
        sudo firmware-util.sh

    Or under Linux: 

        cd; curl -LO https://mrchromebox.tech/firmware-util.sh && sudo bash firmware-util.sh

    __Very important__: you MUST execute this command **as a normal/non-root user**.

    ![](/images/tech/galliumos-install-3.jpg)

1. Next, continue to use the same __firmware-util.sh__ script to install firmware. Should be simple enough. 

    Then, plugin the GalliumOS installation disk into USD, and reboot. 

1. Now start __the actual installation process__ of GalliumOS!

1. Burn the ISO using [BalenaEtcher](https://www.balena.io/etcher/). I used my old Mac to do the job. 

1. Keep your USB drive plugged-in before rebooting. On the "__OS verification is OFF__" screen, press __Ctrl + L__

1. Install GalliumOS (I recommend using the English mode + Wiki connected to install).

1. You may or may not need to press Ctrl + L every time you boot the system, depending on which fireware script you chose to install. 

## [Important] Power Drain

如果电脑突然没电了，你的 Chromebook 无法启动，而是哔哔很大的两声，这说明你的 dev_boot_legacy flag 被 GBB 给 unset 成 0 了。

Sorry to tell you, 你只能恢复原 ChromeOS，然后重来一次了。你的数据都没了。

没别的办法，你猜我怎么知道的？ 

Reference：

> Important: If you choose an ISO install of GalliumOS (thus removing ChromeOS), and choose to use the Legacy Boot Mode of the stock firmware (ie, with the stock or updated RW_LEGACY firmware), and you allow your battery to drain completely, you might have a problem booting GalliumOS. This is due to the Developer Mode boot flag enabling Legacy Boot mode being reset when power is lost - see crossystem flags.
>
> https://wiki.galliumos.org/Firmware#crossystem

How to fix: [必须改 GBB](https://chromium.googlesource.com/chromiumos/platform/vboot/+/master/_vboot_reference/firmware/include/gbb_header.h)，但是不建议直接改 c++ 代码，因为是只读的。最便捷的方法是使用 __MrChromebox's [ChromeOS firmware utility script](https://mrchromebox.tech/#fwscript)__.

# 二、chrx installation

这种模式很好，因为 ChromeOS 被原本保留了。恢复起来也很方便。

主要问题就是硬盘太小。低端Chromebook 普遍采用 32G 的 flash drive。装 ChromeOS 使用一大半，GalliumOS 占用 7-8G，空间就没了。

# Troubleshooting

## 开机画面（dev mode）键盘选项

* __[Ctrl+D]__ to boot ChromeOS in __Developer Mode__, or
* __[Ctrl+L]__ to boot __Legacy Mode__ (usually used for Linux, after installing)
* [Ctrl+U] to boot a ChromeOS (or ChromiumOS) image from USB (you'll never need to use this)
* [TAB] for some boot configuration information

---
title: 【Tech】 Run Jellyfin server on Windows
category: unknown
tags: technology
comments: true
date: 2022-05-05 00:00:00
---


# 注意

记得要选 dir，否则 jellyfin 的文件全都存在 C盘，清理起来很麻烦。

> If you really need to clean up those cache on Windows, it's under:
>
> C:\Users\Admin\AppData\Local\jellyfin

## parameters

jellyfin.exe --help

	Jellyfin.Server 10.7.7.0
	Copyright ?  2019 Jellyfin Contributors. Code released under the GNU General Public License

	  -d, --datadir             Path to use for the data folder (database files, etc.).

	  --nowebclient             Indicates that the web server should not host the web client.

	  -w, --webdir              Path to the Jellyfin web UI resources.

	  -C, --cachedir            Path to use for caching.

	  -c, --configdir           Path to use for configuration data (user settings and pictures).

	  -l, --logdir              Path to use for writing log files.

	  --ffmpeg                  Path to external FFmpeg executable to use in place of default found in
								PATH.

	  --service                 Run as headless service.

	  --package-name            Used when packaging Jellyfin (example, synology).

	  --restartpath             Path to restart script.

	  --restartargs             Arguments for restart script.

	  --published-server-url    Jellyfin Server URL to publish via auto discover process

	  --help                    Display this help screen.

	  --version                 Display version information.

# Command

在桌面上创建一个 bat 文件，内容如下：

	powershell -Command "D:\green\jellyfin-server\jellyfin.exe -d D:\Documents\jellyfin-datadir -w D:\green\jellyfin-web -C D:\Documents\jellyfin-datadir\cache"

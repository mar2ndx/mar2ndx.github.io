---
title: Install Resilio Sync in 2024
category: unknown
tags: []
comments: true
date: 2025-04-16 17:03:28
---

## Overview

Since version 3.0, Resilio requires a license key to run, and it's not backward compatible with version 2.

Thus, let's install version 2.8.1 instead.

## Install on CentOS 7

```bash
curl -O -L --progress-bar https://download-cdn.resilio.com/stable/rpm/x86_64/0/resilio-sync-2.8.1.1390-1.x86_64.rpm

sudo yum install resilio-sync-2.8.1.1390-1.x86_64.rpm
```

## Permissions

Refer to [this post](https://help.resilio.com/hc/en-us/articles/206178924-Installing-Sync-package-on-Linux):

For me, I am 'root' on VPS, so: 

```bash
sudo usermod -aG root rslsync
sudo usermod -aG rslsync root
sudo chmod g+rw /home/rslsync/_resilio/
```

To run: 

```bash
sudo systemctl restart resilio-sync
sudo systemctl enable resilio-sync
```

You should be able to access the web UI at: http://<your_server_ip>:8888/gui. Note it's NOT https, and the `/gui` at the end, very important.

## Set to http-only

Set to http-only to avoid "Too many redirects" error on Cloudflare.

```bash
vi /etc/resilio-sync/config.json
```

Also, allow remote access by setting `listen` to `0.0.0.0:8888`.

```json
{
    "storage_path" : "/home/rslsync/",
    "pid_file" : "/var/run/resilio-sync/sync.pid",

    "webui" :
    {
        "force_https": false,
        "listen" : "0.0.0.0:8888"
    }
}
```

## Debug Resilio

Check status:

```bash
sudo journalctl -u resilio-sync
systemctl status resilio-sync
```

Check Web UI:

```bash
curl -k -L http://127.0.0.1:8888/gui
# you might get: Sync does not support your web browser.
wget --no-check-certificate -q -O - http://127.0.0.1:8888/gui
# you might get: For your security, please use a current version of Chrome or Firefox.
```

# Reference

https://unclemartian.github.io/2022/03/25/Tech/ubuntu/install-resilio-sync/

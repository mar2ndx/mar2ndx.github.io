---
title: 【Tech】 curl download a batch of files on Linux
category: unknown
tags: ubuntu
comments: true
date: 2022-04-19 00:00:00
---


# Download 1 file

    curl -O https://example.com/files/README

Or

    curl -o my-readme-file https://example.com/files/README

# Download many files async

    curl \
        -o file-name-1 https://example.com/files/file-1 \
        -o file-name-2 https://example.com/files/file-2

## Reference

https://hackernoon.com/how-to-download-a-file-using-curl-with-examples-mon3ubd

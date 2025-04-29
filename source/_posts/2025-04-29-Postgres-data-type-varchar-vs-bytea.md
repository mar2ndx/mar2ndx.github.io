---
title: Postgres data type varchar vs bytea
category: unknown
tags: []
comments: true
date: 2025-04-29 20:25:57
---

I need to store some hash value with SHA-256 encryption. 

> SHA-256

What Data Type should I use? 

## varchar(64)

Each character is stored as 1 byte (if using standard ASCII/UTF-8). Total bytes: 64 bytes (= 512 bits).

This is more than needed to store the true SHA-256 hash, since the original hash is only 32 bytes (256 bits). 

The overhead comes from encoding as hex.

## bytea

This is PostgreSQL’s type for storing binary data.
If you store the raw output of SHA-256, it is exactly 32 bytes (since the hash is 256 bits).
Total bytes: 32 bytes
Total bits: 32 × 8 = 256 bits
This is as compact as possible, no extra storage overhead for encoding.

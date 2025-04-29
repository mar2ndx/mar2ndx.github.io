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

for PostgreSQL, this is raw output of SHA-256, it is exactly 32 bytes. Total bits: 32 × 8 = 256 bits.

This is as compact as possible, no extra storage overhead for encoding.

# Conclusion

bytea: Use for best storage efficiency. Store the plain binary hash.

varchar(64): Use if you absolutely need a hex string for human readability or simple debugging, but it consumes twice the space.

--- 

When you store a hex string as text (e.g., "b1a89231..."), each character is a hex digit.
If the string is plain ASCII (which is always the case for hex: only 0-9, A-F), each character is 1 byte in almost all encodings (including UTF-8, ASCII, Latin1).

UTF-8 stores ASCII characters in 1 byte per character, so a 64-character hex string is 64 bytes (when encoded/saved).

---
title: "[Design] How to Design Logging"
category: Design
tags: []
comments: true
date: 2016-08-01 00:00
---


# Logging

Conecting between **information** and **knowledge**.

1. Information: it's just bits
2. **Knowledge**: drives product direction

## Logging is all about Event

Q1. shall we log it live? what should we log? how to do it (on different platforms)?

Not live. Do it asynchronously.

**Demand and product design** drives logging.

Logs represent event, so all your logging should be **based around the events**.

> eg. who click the button, the user ID, but do not log the age, because you can find it somewhere else!

## Think about "what" to log and "why"

**"How" is just coding**. Happy Logging!

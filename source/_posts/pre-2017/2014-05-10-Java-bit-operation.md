---
title: "[Fundamental] Java Bit Operation "
category: Fundamental
tags: []
comments: true
date: 2014-05-10 00:00
---


### Bit operators

<table border="2">
  <tr>
    <th>operator</th>
    <th>what is means</th>
  </tr>
  <tr>
    <td>~</td>
    <td>invert every bit</td>
  </tr>
  <tr>
    <td>&lt;&lt;</td>
    <td>shift left (same as *2)</td>
  </tr>
  <tr>
    <td>&gt;&gt;</td>
    <td>signed shift right</td>
  </tr>
  <tr>
    <td>&gt;&gt;&gt;</td>
    <td>unsigned shift right</td>
  </tr>
  <tr>
    <td>^</td>
    <td>XOR</td>
  </tr>
  <tr>
    <td>|</td>
    <td>OR</td>
  </tr>
</table>
<br />

Note the unsigned right shift operator ">>>" shifts a **zero into the leftmost position**, while the leftmost position after ">>" **depends on sign extension**.

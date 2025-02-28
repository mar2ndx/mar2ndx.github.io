---
title: "[Java OOP] Java modifier and Access Level"
category: Java OOP
tags: []
comments: true
date: 2014-06-14 00:00
---


## 4 Types of Access Level

#### Private

Like you'd think, only the class in which it is declared can see it.

#### Package Private (default)

Can only be seen and used by the package in which it was declared.

This is the default in Java (which some see as a mistake).

#### Protected

Package Private, plus can be seen by subclasses.

#### Public

Everyone can see it.

## Differences

![](/images/java-access-level-table.png)

**Note**: Java default access setting is 'No modifier', which is also called '**Package Private**'.

**Another note**: by saying 'subclass', it means subclass declared in **another package**.

#### Example

Class structure:

![](/images/java-classes-access-level.gif)

For the methods of 'Alpha' class, the visibility is listed below.

For example, Gamma can only access public methods in Alpha.

<table class="tg">
  <tr>
    <th class="tg-031e">Modifier</th>
    <th class="tg-031e">Alpha</th>
    <th class="tg-031e">Beta</th>
    <th class="tg-031e">Alphasub</th>
    <th class="tg-031e">Gamma</th>
  </tr>
  <tr>
    <td class="tg-031e">public</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
  </tr>
  <tr>
    <td class="tg-031e">protected</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">N</td>
  </tr>
  <tr>
    <td class="tg-031e">no modifier</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">N</td>
    <td class="tg-031e">N</td>
  </tr>
  <tr>
    <td class="tg-031e">private</td>
    <td class="tg-031e">Y</td>
    <td class="tg-031e">N</td>
    <td class="tg-031e">N</td>
    <td class="tg-031e">N</td>
  </tr>
</table>
<br />

## Additional question

#### Can we declare a top-level class as private?

Answer: No, Java does not allow top-level private class. Think about it, a top-level class as private would be useless because nothing could access it.

If you really want, you can use inner or nested classes. If you have a private inner or nested class, then access is restricted to the scope of that outer class.

[link](http://stackoverflow.com/questions/1913863/java-why-can-we-define-a-top-level-class-as-private)

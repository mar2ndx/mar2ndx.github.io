---
title: SpringMVC learning notes
comments: true
category: Design
tags: []
---

# Spring MVC

# Getting Started

## B/S vs C/S

C/S架构，已经过时了。

B/S架构 --> web应用。

## 其中的 S = web application

JavaEE 制定了一套规范，很简单实现了 B/S 的沟通（结构处理）。

> 这套规范，就是servlet。“服务器端 小程序”

Java开发 web应用：需要遵循__三层架构__：

1. 表现层
1. 业务层
1. 持久层

Spring MVC 只跟 1. 表现层 有关。

## web应用 三层架构

### 1 表现层（web层）

web层，跟browser打交道。

1. 接收 http request
1. http 响应 response
1. 以及：分发请求

继续细分的话：

1. 展示层：jsp
1. 控制层：controller，struts2 那种action

表现层的设计，通常使用 MVC设计模型（这里的MVC和其他层没有关系）。

### 2 业务层（service层）

也就是 service 层。

web层依赖service，但是service层不依赖web。

负责业务逻辑

### 3 持久层（dao层）

跟DB有关的一切，也就是dao层。

也就是jdbc，mybatis。

跟service层无关系。

## MVC 设计模式

MVC __不是__ JavaEE 的23 种设计模式之一。

只是针对：__表现层__的。

### 1 Model

不仅是数据存储。其实，分两种：

1. 业务模型
1. 数据模型

### 2 View

通常的jsp，通常是根据model创建的。

### 3 Controller

控制：数据流向。

流向哪个业务处理 class。

# Spring MVC

“一个轻量级的web框架。”

## 跟Spring 的关系和区别

Spring MVC 是 Spring Framework 的一部分。

* Spring Framework
    * Core
    * AOP
        * DAO
        * ORM
    * JEE
    * Web
        * Spring MVC 在这里
        
可见，Spring MVC 是 Spring 下面的 Web 模块的一个成员。

### 支持Spring的MVC 框架

Spring MVC 不是唯一的。还有 Struts1（小众） 和 Struts2。

### 特点

RestFul 的支持好，所以 微服务 喜欢用。
---
title: MyBatis and SSM (Spring/SpringMVC/MyBatis)
category: Design
tags: []
comments: true
date: 2022-11-01 04:35
---


# MyBatis

MyBatis是一个持久层框架（persistence framework), 封装了JDBC的原装代码：

1. 定制化SQL
1. 存储过程
1. 高级映射

> Persistence framework 也是 Object-Relational Mapping (ORM) 工具。
>
> MyBatis provides a mapping engine that maps SQL results to object trees in a declarative way. 

## 软件开发3层：SSM框架

1. 表现层 SpringMVC
1. 业务层 Spring
1. 持久层 MyBatis

## SSM框架

SSM框架是spring MVC ，spring和mybatis框架的整合，是标准的MVC模式，将整个系统划分为表现层，controller层，service层，DAO层四层，使用spring MVC负责请求的转发和视图管理，spring实现业务对象管理，mybatis作为数据对象的持久化引擎

相比于之前的SSH（Spring+Struts+Hibernate），SSM更加轻量化和灵活，是目前业界主流的Java Web开发框架。

## Spring

简单来说，Spring是一个轻量级的控制反转（IoC）和面向切面（AOP）的容器框架。

## SpringMVC

SpringMVC把传统的模型层被拆分为了业务层(Service)和数据访问层（DAO,Data Access Object）。

## MyBatis

MyBatis 是一款优秀的Java持久层框架(persistence framework)，它支持定制化 SQL、存储过程以及高级映射。MyBatis 消除了几乎所有的JDBC代码和参数的手工设置以及结果集的检索。MyBatis 使用简单的 XML配置文件或注解，将接口和 Java 的POJOs（Plain Old Java Objects，普通的 Java对象）映射成数据库中的记录。

## MyBatis 缓存

一级缓存：sql session级别的。eg 同一个 findUserById（），多次调用，只要之间没有过数据写入操作，就可以直接调用缓存。

二级缓存：是Mapper（namespace）级别。默认不开启（因为crud概率很高，所以缓存意义不大）。

如果要开启二级缓存，则 class 需要 implements Sezerialzed。

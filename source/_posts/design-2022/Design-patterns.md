---
title: Java Design Pattern
comments: true
category: Design
tags: []
---

# 开篇

__GoF__ - 23 种设计模式。

> The four authors **Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides** are collectively introduced the **Gang of Four Design Patterns** in Software development. 
>
> In 1994, they published a book (Design Patterns: Elements of Reusable Object-Oriented Software) for explaining the concept of Design Patterns.

设计模式是 __面向对象__的。

## Why 设计模式？

答：利用前人的经验，解决现在的问题。

# 设计原则

__设计模式__：是按照 __设计原则__ 进行实践的方式和方法

    eg. **one country** 是原则，不可改变。

    但是，**one country, two system** 是方式方法，是可以聊的。

# 7种设计原理

1. 开闭原则
    * 是总纲。
    * 对**扩展开放**，对**修改关闭**
1. 单一职责
    * 对于class而言。
    * 一个类，不能太累。
    * Class一定要功能单一。
    * 例如经典的 3 class MVC：DBUtil用于获取连接；CustomerDAO用于查询；CustomerDataChart用于打印报表。
1. 接口隔离
    * 对于interface而言。
    * 不要让一个接口有太多功能。
    * 这样压力太大了。
1. 李氏代换
    * 不用破坏继承体系。
    * 尽量不要改parent已经实现的方法。
    * 而是通过添加新方法，扩展父类的功能。
    * 例如父类：class parent {m1(){ print 父亲 }} 
    * 子类：class child { m2(){ m1(); // something else; }}
1. 依赖倒置
    * 面向接口/抽象 去编程。
    * 不要面向实现/细节 而编程。
    * 对于param，return value 等，都使用interface，abstract，而不是具体实现。
    * eg. Dog 实现了Animal，但是返回type，依然是返回 Animal。
1. 合成复用
    * 优先使用组合 / 聚合复用
    * 如果能用 组合/聚合 关系，就不用 继承。
    * 例如：class A { B, C public void method2(){ B.method1(); // 功能增强} }
    * A 不需要 继承 B/C
1. 最少认知原则 （迪米特法则 Demeter / LKP）
    * 降低耦合度。
    * 不用和陌生人交流。
    * 不要这么写：class UserService { CustomerService service = ... }
    * 而是：class UserService { UserDao dao = ... } 然后通过第三者（中间人）来沟通

# Design Pattern 的 3 类型

一共23种类型：

1. 创建类：5种
1. 结构类：7种
1. 行为类：11种

其中，最重要的只有10种：

1. 创建类 x5
    1. 工厂
    1. 抽象工厂
    1. 原型模式
    1. 构建者
    1. 单例
1. 结构类 x3
    1. 适配器
    1. 装饰模式
    1. 代理
    1. （仅需要了解）组合模式
1. 行为类 x2
    1. 模版方法
    1. 策略模式
    1. （仅需要了解）责任链

其中，Singlton单例，最简单也最难。因为考的其实是 thread safety (线程安全)。

# 创建类 Design Pattern

## 区别

1. 工厂模式  ：批量生产（属性一致）
1. 构建者模式：私人订制（属性不一致）
1. 单例模式  ：只生产一个
1. 原型模式  ：给我一个object，我创建一个相同的（山寨版）

## 创建类 一二、Factory

When to use？

1. 我对搞对象不感兴趣，我只想使用对象。
1. 当对象的构造需要many parameter，非常复杂。
1. 对象是3rd party jar包提供的，我不知道怎么传参。

Factory 分为3种：

1. 简单工厂
	1. 上帝工厂：给我一个参数，我给你一个对象。
	1. 静态方法工厂：跟上帝差不多，只不过避免了传参错误的问题。
	1. 简单工厂模式，简单粗暴，可以实例化任何产品。但是：负担太重，不合符开闭原则。
1. 工厂方法模式
	1. 并不构建，而是给你一个 factory instance。
	1. 你拿到factory实例，再自己构建产品。
1. 抽象方法
	1. 类似工厂方法
	1. 需要一套实例（而不是一个），所以工厂需要抽象化。
	1. 什么牌子的工厂，生产什么牌子的轮胎。

## 创建类 三、原型模式 

给我一个原型，我给你一个对象。（copy）

例如：BeanUtils.copy（）

1. 浅拷贝：只复制非引用类型的属性。
1. 深拷贝：对 reference type也拷贝。

深浅拷贝，如何实现的？

1. shallowCopy：实现 Clonable 接口，然后super.clone() 就行了。
1. deepCopy：需要用到 Serializable 对 object 进行输出和读取。

## 创建类 四、构建者

根据客户的需求，创建指定对象。

例如：

```
// 构建者模式
StudentBuilder.id(123).name("Jordan").age(25).build();
```

## 创建类 五、Singleton

全局之中，只构建一个实例。

Spring大多数对象都是 Singleton，一般被spring管理的bean，都是业务对象，不是数据对象。

分2种：

1. 饿汉式：线程安全的。但是会造成资源浪费。
1. 懒汉式（lazy loading）：不安全。

实现方法：

1. constructor（） 私有
1. static成员变量 也是私有
1. public static 方法：获取静态成员变量

为什么饿汉式是thread-safe？因为JVM加载一个class的时候，过程默认加锁。

```
public class SingletonDemo {
    private static SingletonDemo instance = null;
    private SingletonDemo() { }
    public static synchronized SingletonDemo getInstance() {
        if (instance == null) {
            instance = new SingletonDemo();
        }
        return instance;
    }
}
```

但是，以上的“方法锁”，效率不高。所以：

```
public class SingletonDemo {
    private static volatile SingletonDemo instance = null;
    private SingletonDemo() { }
    public static SingletonDemo getInstance() {
        if (instance == null) {
            synchronized (SingletonDemo.class) {
                if (instance == null) {
                    instance = new SingletonDemo();
                }
            }
        }
        return instance;
    }
}
```

### 关于 volatile

并发编程的3大特性：（了解就行）

1 原子性
2 有序性
3 可见性。

Volatile的功能：

1. 禁止被它修饰的变量相关操作进行指令(Just-In-Time JIT compiler)重排序。

		理解一个对象在内存中的创建过程：Student student = new Student();
		底层字节码的执行过程（有序性）
					
		1.new 会触发类加载机制（已经被加载过的类不需要再次加载）
		2.分配堆内存空间（相当于已经有内存地址）
		3.将对象进行初始化（将成员变量初始化为0）
		4.将对象引用地址赋值给栈空间中的变量
		JVM的JIT即时编译器会对代码的执行过程进行优化，包含代码的执行顺序。
		也就是说以上对象的创建过程，可能被JIT即时编译器优化为1-2-4-3（指令重排序）。

1. 禁止CPU使用缓存（工作内存），直接操作内存。

		eg. i++ 不是原子性操作。

		1.先从局部变量表中获取i的值
		2.将i的值加入到操作栈中
		3.将操作栈中的i进行自加
		4.将自加的i值放入操作栈
		5.将操作栈的栈顶元素取出并放入局部变量表
		
		如何保证原子性呢？
		答：使用锁机制（synchronized和lock锁）

#结构类

1. 适配器

TODO

1. 装饰模式

TODO

1. 代理

TODO

# 行为类

1. 模版方法

TODO

1. 策略模式

TODO

# 系统设计

## 设计模式

### 你知道有哪些设计模式吗？

+ 创建型模式
    + 工厂方法模式
    + 抽象工厂模式
    + 单例模式
    + 建造者模式
    + 原型模式
+ 结构型模式
    + 适配器模式
    + 桥接模式
    + 装饰器模式
    + 组合模式
    + 外观模式
    + 享元模式
    + 代理模式
+ 行为型模式
    + 模板方法模式
    + 命令模式
    + 迭代器模式
    + 观察者模式
    + 中介者模式
    + 备忘录模式
    + 解释器模式
    + 状态模式
    + 策略模式
    + 职责链模式
    + 访问者模式

### 什么是创建型模式、结构型模式、行为型模式？

+ 创建型模式是处理对象创建的设计模式，试图根据实际情况使用合适的方式创建对象。

+ 结构型模式是处理类或对象的组合的设计模式。

+ 行为型模式是对在不同的对象之间划分责任和算法的抽象化。

### 你知道有哪些设计原则吗？

+ 单一职责原则：一个类只负责一个功能领域中的相应职责。

+ 开闭原则：软件实体应对扩展开放，而对修改关闭。

+ 里氏代换原则：所有引用基类对象的地方能够透明地使用其子类的对象。

+ 依赖倒转原则：依赖于抽象而不是具体。

+ 接口隔离原则：不应当将一个大而全的接口放在应用层，应用层的接口应当设计得比较小，并且要考虑到客户端的具体需要。

+ 迪米特法则：一个实体应当尽量少地与其他实体之间发生相互作用，使系统功能模块相对独立。

+ 合成复用原则：尽量使用合成/聚合的方式，而不是使用继承。

### 谈谈单例模式

+ 单例模式确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例。

+ Python 中应用单例模式的实际场景：
    
    + 数据库连接池
    + 日志记录器
    + 线程池
    + 全局配置对象
    + 对象缓存

+ Python 中实现单例模式的方法有很多，可以使用模块、装饰器、元类等：

    + 使用模块

        ```python
        # mysingleton.py
        class My_Singleton(object):
            def foo(self):
                pass

        my_singleton = My_Singleton()
        ```

        ```python
        # to use
        from mysingleton import my_singleton

        my_singleton.foo()
        ```

    + 使用装饰器

        ```python
        from functools import wraps

        def singleton(cls):
            instances = {}
            @wraps(cls)
            def getinstance(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            return getinstance

        @singleton
        class MyClass(object):
            pass
        ```

    + 使用元类

        ```python
        class Singleton(type):
            def __init__(cls, name, bases, dict):
                super(Singleton, cls).__init__(name, bases, dict)
                cls._instance = None

            def __call__(cls, *args, **kwargs):
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
                return cls._instance

        class MyClass(object):
            __metaclass__ = Singleton
        ```

### 请你谈谈你的系统设计经验



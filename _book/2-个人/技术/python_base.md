# Python 语言

## Python 语言基础


### 谈谈你认为的 Python 语言的优缺点

+ 胶水语言，轮子多，应用广泛。

+ 语言灵活，生产力高

+ 缺点是性能问题、代码维护问题、2/3 版本兼容问题。

### Python 是静态还是动态类型？是强类型还是弱类型？

+ 动态还是静态指的是变量的类型是在编译时确定还是在运行时确定。

+ Python 是动态类型语言，变量的类型是在运行时确定的。

+ 强类型还是弱类型指的是变量的类型转换是否受限制，会不会发生隐式类型转换。

+ Python 是强类型语言，不同类型的变量不能直接进行运算，需要进行类型转换。

### 什么是鸭子类型？

+ 有一句话是："如果你看到一只鸟，走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子。"

+ 鸭子类型是一种动态类型的风格，是多态的一种形式。

+ 关注的是对象的行为，而不是对象的类型。

+ 常见的应用场景就是：Python 中的迭代器协议，只要对象实现了 `__iter__` 和 `__next__` 方法，那么这个对象就是可迭代的。

### 什么是 monkey patch？

+ monkey patch 是指在运行时动态修改一个类或模块，即运行时替换。

    ```python
    import time
    print(time.time())

    def new_time():
        return 1234567890.0
    
    # monkey patch
    time.time = new_time
    print(time.time())
    ```

+ 比如 gevent 就是通过 monkey patch 来实现协程的。

    ```python
    import socket
    print(socket.socket)

    from gevent import monkey
    monkey.patch_socket()
    print(socket.socket)
    ```

### 什么是自省（introspection）？

+ 自省就是运行时判断一个对象类型的能力。

+ Python 中的自省机制包括：`id()`、`type()`、`isinstance()`、`dir()`、`hasattr()`、`callable()`、`issubclass()`。

+ Inspect 模块也提供了很多自省的函数。

+ 自省的应用场景：动态导入模块、动态实例化类、动态获取类的成员。

### 你知道 Python 之禅是什么吗？

+ Python 之禅是 Python 的设计哲学，是 Python 语言的核心。

+ 通过 `import this` 可以查看 Python 之禅。

+ 因为动态语言编写大型项目的可维护性不高，所以 Python 之禅强调的是可读性以及可维护性。

## Python 2 and Python3

### Python 2 和 Python 3 的区别

+ Python 2 默认编码是 ASCII，Python 3 默认编码是 UTF-8

+ Python 2 的 print 是一个语句，Python 3 的 print 是一个函数

+ Python 2 的整数除法是向下取整返回一个整型，Python 3 的整数除法是向零取整返回一个浮点型

### Python 3 的改进

+ 提供了很多方便的语法糖，比如解包、类型注解

+ 内置函数之前返回列表的现在全部返回为迭代器，节省了内存

+ 提供了异步编程的支持

### 兼容 2/3 版本的工具

+ six 模块，提供了语法兼容工具

+ 2to3 工具，可以将 Python 2 代码转换为 Python 3 代码

+ __future__ 模块，可以在 Python 2 中使用 Python 3 的特性

## Python 函数

### 什么是 Python 中的可变对象和不可变对象

+ 可变对象：列表、字典、集合、自定义类

+ 不可变对象：数字、字符串、元组、布尔值、None、frozenset、bytes

+ Python 中一切皆对象，变量是对象的引用。可变对象作为参数传递时，传递的是对象的引用，所以在函数内部修改了可变对象，会影响到函数外部的对象。不可变对象作为参数传递时，传递的是对象的值，所以在函数内部修改了不可变对象，不会影响到函数外部的对象，并且生成了一个新的对象。

### Python 中 *args 和 **kwargs 的作用

+ *args：将位置参数打包成 tuple 给函数体调用，可以通过列表或元组解包的方式传递位置参数给函数

+ **kwargs：将关键字参数打包成 dict 给函数体调用，可以通过字典解包的方式传递关键字参数给函数


### 装饰器主要实现逻辑

+ 装饰器的本质是一个函数，它接收一个函数作为参数，然后返回一个函数。

+ 装饰器的作用是在不改变原函数的情况下，为原函数添加新的功能。

+ 实现代码如下：

    ```python
    def decorator(func):
        def wrapper(*args, **kwargs):
            # do something
            return func(*args, **kwargs)
        return wrapper

    @decorator
    def func():
        pass
    ```

## Python 异常

### Python 中的异常处理机制

+ Python 中的异常处理机制是 try-except-else-finally 语句。

### 为什么自定义异常通常是继承 Exception 而不是继承 BaseException

+ BaseException 是所有内置异常的基类，而 Exception 是所有内置非系统退出异常的基类。

+ 自定义异常通常是继承 Exception，因为 BaseException 包含了系统退出异常，如果自定义异常继承 BaseException，那么这个自定义异常就会被系统退出异常捕获，从而导致程序退出。

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ...
```



# Python Web

## Python Web 基础

### 什么是 WSGI？

+ WSGI 是 Web Server Gateway Interface 的缩写，即 Web 服务器网关接口。

+ WSGI 是 Python Web 服务器和 Web 框架/应用程序之间的一种接口标准，实现了 Web 服务器和 Web 应用程序之间的解耦。

+ WSGI 的具体规范可以参考 [PEP 3333](https://www.python.org/dev/peps/pep-3333/)。

+ WSGI 的本质是一个 `callbale`，即一个可调用对象，它接收两个参数，一个是包含了 CGI 环境变量的字典，一个是 `start_response` 回调函数。

### 网关接口是啥意思？

+ 网关接口是指 Web 服务器和 Web 应用程序之间的接口。

+ web 服务器：比如 Nginx、Apache、IIS 等。

+ Web 应用程序：比如 Django、Flask、Tornado 等。

+ Web 服务器和 Web 应用程序之间的接口有很多种，比如 CGI、FastCGI、SCGI、WSGI、uWSGI、ASGI 等。

## flask


### flask 中的上下文是什么？

+ flask 中的上下文是指：请求上下文和应用上下文。

+ 请求上下文：
    + 请求上下文是指：在处理请求之前，flask 会创建一个请求上下文对象，它封装了客户端发送的 HTTP 请求信息，比如请求头、请求体等。
    + 请求上下文对象是一个全局对象，它的生命周期是：在请求开始时创建，在请求结束时销毁。

+ 应用上下文：
    + 应用上下文是指：在处理请求之前，flask 会创建一个应用上下文对象，它封装了 flask 应用程序的信息，比如配置信息、数据库连接等。
    + 应用上下文对象是一个全局对象，它的生命周期是：在应用程序启动时创建，在应用程序结束时销毁。


### flask 框架中的蓝图是什么？

+ 蓝图是 flask 框架中的一个组件，它可以将一个应用程序分割成多个模块，每个模块都可以单独编写，然后注册到应用程序中。

+ 蓝图的作用是：
    
    + 1. 可以将一个复杂的应用程序划分为多个模块，每个模块可以单独管理。
    + 2. 方便代码的管理和维护。
    + 3. 可以将一个应用程序分发给多个开发人员协同开发。

+ 具体代码实现：

    ```python
    # 导入蓝图对象
    from flask import Blueprint

    # 创建蓝图对象
    app = Blueprint('app', __name__)

    # 注册蓝图对象到应用程序中
    app.register_blueprint(app)
    ```

## django

### django 那些用到了单例模式

+ django 的 `settings` 模块就是一个单例模式，它的实现代码如下：

### django 中权限管理是如何实现的？

+ django 中的权限管理是通过 `django.contrib.auth` 模块实现的。

+ 实现的原理是：

+ 权限的认证是基于 `django.contrib.auth.backends.ModelBackend` 模块实现的。

+ 通过继承 ModelBackend 重载 authenticate 方法实现自定义认证。

+ 使用方法是：


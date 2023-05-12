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

# django 那些用到了单例模式

+ django 的 `settings` 模块就是一个单例模式，它的实现代码如下：

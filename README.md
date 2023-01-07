# gitbook-demo

> 应用此项目，您可以快速构建您的 gitbook 项目。

### 如何使用

1. 创建 github 仓库，并将此项目复制到仓库中。

1. 在仓库中创建 gh-pages 分支，用于发布 gitbook。

1. 使用编辑器在 docs 目录下编写 gitbook 相关内容。

1. 使用 shell 运行 deploy.sh 脚本。

1. 在 github 该仓库下，进入 Settings > Pages > Build and deployment > Branch，选择 gh-pages 分支，/(root) 路径，并保存。

1. 通过 username.github.io/reponame 访问 gitbook。eg: <https://fmw666.github.io/gitbook-demo/>

### 附录

gitbook 使用教程：<http://caibaojian.com/gitbook/>

gitbook 常用命令：

```sh
# 安装插件
gitbook install

# 编译
gitbook build

# 启动本地服务 
gitbook serve
```

gitbook 常用插件：<https://www.jianshu.com/p/09bf890ec8f6>

Requirements
--------
使您的 MCDReforged 插件无需用户手动安装 Python 软件包！

## 特点

 - 自动安装缺失的软件包
 - 可调整的 PyPI 镜像源
 - 可内置到您的插件中

## 适配

适配非常简单！只需要在您插件的 [on_load()](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#plugin-loaded) 函数中略作改动。

参见[示例](#示例)与[调用方法](#调用方法)。

## 示例

例如安装 [Request](https://pypi.org/project/requests/) 库：

```
def on_load(server: PluginServerInterface, prev_module):
    server.get_plugin_instance('requirements').installModule(server, 'requests')
    import request
    ...
```

或者是批量安装：

```
def on_load(server: PluginServerInterface, prev_module):
    server.get_plugin_instance('requirements').installModules(server, ['requests', 'pymysql', 'smtplib'])
    import request
    import pymysql
    import smtplib
    ...
```

甚至直接调用 requirements.txt：

```
def on_load(server: PluginServerInterface, prev_module):
    server.get_plugin_instance('requirements').installModulesFromFile(server, 'https://raw.githubusercontent.com/MCDReforged/MCDR-bot/master/requirements.txt')
    import cryptography
    import requests
    import PyNBT
    ...
```

您也可以提取 __init__.py 文件，并将其嵌入您的插件中。

## 调用方法

```
def installModule(server: PluginServerInterface, moduleName: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    ...

def installModules(server: PluginServerInterface, modulesList: list, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    ...

def installModulesFromFile(server: PluginServerInterface, filePath: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    ...
```


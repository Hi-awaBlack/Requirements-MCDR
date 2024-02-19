Requirements
--------
Make your MCDReforged plugin free of the need for users to manually install Python packages!

## Features

  - Automatically install missing packages
  - Adjustable PyPI mirror source
  - Can be built into your plugin

## Adaptation

Adaptation is very easy! Just make a slight change in your plugin's [on_load()](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#plugin-loaded) function.

See [Example](#Example) and [Calling Method](#Call Method).

## Example

For example, install the [Request](https://pypi.org/project/requests/) library:

```
def on_load(server: PluginServerInterface, prev_module):
     server.get_plugin_instance('requirements').installModule(server, 'requests')
     import request
     ...
```

Or batch installation:

```
def on_load(server: PluginServerInterface, prev_module):
     server.get_plugin_instance('requirements').installModules(server, ['requests', 'pymysql', 'smtplib'])
     import request
     importpymysql
     import smtplib
     ...
```

Or even call requirements.txt directly:

```
def on_load(server: PluginServerInterface, prev_module):
     server.get_plugin_instance('requirements').installModulesFromFile(server, 'https://raw.githubusercontent.com/MCDReforged/MCDR-bot/master/requirements.txt')
     import cryptography
     import requests
     importPyNBT
     ...
```

You can also extract the __init__.py file and embed it in your plugin.

## Call method

```
def installModule(server: PluginServerInterface, moduleName: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
     ...

def installModules(server: PluginServerInterface, modulesList: list, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
     ...

def installModulesFromFile(server: PluginServerInterface, filePath: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
     ...
```
Requirements
--------

**简体中文** | [`English`](README.md)

使您的 MCDReforged 插件无需用户手动安装 Python 软件包！

## 特点

  - 自动安装缺失的软件包
  - 可变的 PyPI 源
  - 简单的适配

## 适配

适配非常简单！只需要对您的插件略作改动。

### 导入

#### 依赖形式

如果 Requirements 插件是以 MCDReforged 插件形式存在的，可以使用以下方法导入：

```python
# 推荐
import requirements

# 不推荐
requirements = server.get_plugin_instance('requirements')
```

请注意在您插件的[元数据](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/metadata.html)中声明依赖项！

#### 嵌入形式

您也可以提取本插件中 `/requirement/__init__.py` 文件，并将其插入您的插件中，即可按正常方法导入。

### 使用

对 Python 软件包的安装应当在 [`on_load`](https://docs.mcdreforged.com/zh-cn/latest/plugin_dev/event.html#plugin-loaded) 事件中操作！

`install_module` 函数可以单独安装一个软件包，将返回代表安装结果的布尔值，就像这样：

```python
def on_load(server, prev):
    success = requirements.install_module(server=server, module_name='requests', pypi_source=requirements.PYPI_OFFICIAL_SOURCE)
    # >                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # >                                                                          这一部分不是必须的，因为存在与本示例相同的默认值。此处演示如何自定义 PyPI 源。
    if not success:
        # 尝试更换 PyPI 源重试
        # 或抛出异常退出程序
        ...

    import requests
    ...
```

`install_modules` 函数可以一次性安装许多软件包，将返回代表安装结果的布尔值，就像这样：

```python
def on_load(server, prev):
    success = requirements.install_modules(server=server, modules_list=['requests', 'sqlalchemy'])
    if not success:
        ...
    
    import requests
    import sqlalchemy
    ...
```

`install_modules_from_file` 函数允许通过 `requirements.txt` 安装软件包，将返回代表安装结果的布尔值，就像这样：

```python
def on_load(server, prev):
    success = requirements.install_modules_from_file(server=server, file_path='https://raw.githubusercontent.com/MCDReforged/MCDR-bot/master/requirements.txt')
    # >                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # >                                                             是的，可以直接通过网络安装。您也可以使用本地文件，但需要确保路径是正确的，当心相对路径！
    if not success:
        ...
    
    import requests
    import sqlalchemy
    ...
```

## 注意事项

 - 安装过程中将堵塞 MCDReforged 主线程

## 参考源代码

```python
from mcdreforged.api.types import PluginServerInterface

PYPI_OFFICIAL_SOURCE = "https://pypi.org/simple/"


def install_module(
    server: PluginServerInterface,
    module_name: str,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    ...


def install_modules(
    server: PluginServerInterface,
    modules_list: list,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    ...


def install_modules_from_file(
    server: PluginServerInterface,
    file_path: str,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    ...
```
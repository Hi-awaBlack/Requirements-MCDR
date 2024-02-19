from mcdreforged.api.types import PluginServerInterface
import importlib
import subprocess


def installModule(server: PluginServerInterface, moduleName: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    try:
        importlib.import_module(moduleName)
    except ImportError:
        try:
            subprocess.check_call(['pip', 'install', '-i', mirrorSource, moduleName])
            server.logger.info(f'Installation of dependency {moduleName} successful.')
        except subprocess.CalledProcessError:
            server.logger.critical(f'Failed to install dependency {moduleName}.')

def installModules(server: PluginServerInterface, modulesList: list, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    for moduleName in modulesList:
        installModule(server=server, moduleName=moduleName, mirrorSource=mirrorSource)

def installModulesFromFile(server: PluginServerInterface, filePath: str, mirrorSource: str = 'https://mirrors.cloud.tencent.com/pypi/simple/'):
    try:
        subprocess.check_call(['pip', 'install','-r',filePath,'-i', mirrorSource])
        server.logger.info(f'Installation of dependencies successful.')
    except subprocess.CalledProcessError:
        server.logger.critical(f'Failed to install dependencise.')
from mcdreforged.api.types import PluginServerInterface
import importlib
import subprocess
import sys

PYPI_OFFICIAL_SOURCE = "https://pypi.org/simple/"


def install_module(
    server: PluginServerInterface,
    module_name: str,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    try:
        importlib.import_module(module_name)
    except ImportError:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-i", pypi_source, module_name]
            )
            server.logger.info(f"Successfully installed {module_name}.")
            return True
        except subprocess.CalledProcessError:
            server.logger.critical(f"Failed to install dependency {module_name}.")
            return False


def install_modules(
    server: PluginServerInterface,
    modules_list: list,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    have_fail = False
    for module_name in modules_list:
        if (
            install_module(
                server=server, module_name=module_name, pypi_source=pypi_source
            )
            is False
        ):
            have_fail = True
    return have_fail


def install_modules_from_file(
    server: PluginServerInterface,
    file_path: str,
    pypi_source: str = PYPI_OFFICIAL_SOURCE,
) -> bool:
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", file_path, "-i", pypi_source]
        )
        server.logger.info(f"Installation of dependencies successful.")
        return True
    except subprocess.CalledProcessError:
        server.logger.critical(f"Failed to install dependencies.")
        return False

# Stubs for moonlighthelper (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, List
from xbmcswift2 import Plugin

from resources.lib.core.logger import Logger
from resources.lib.model.inputdevice import InputDevice
from resources.lib.model.nvapp import NvApp
from resources.lib.service.hostcontextservice import HostContextService
from resources.lib.util.confighelper import ConfigHelper
from xbmcgui import DialogProgress


def loop_lines(dialog, iterator): ...

class MoonlightHelper:
    regex_connect = ... # type: str
    regex_moonlight = ... # type: str
    regex_certificate_gen = ... # type: str
    regex_connection_failed = ... # type: str
    plugin = ... # type: Plugin
    config_helper = ... # type: ConfigHelper
    logger = ... # type: Logger
    internal_path = ... # type: str
    host_context_service = ... # type: HostContextService
    def __init__(self, plugin: Plugin, config_helper: ConfigHelper, logger: Logger) -> None: ...
    def create_ctrl_map(self, dialog: DialogProgress, map_file: str) -> bool: ...
    def create_ctrl_map_new(self, dialog: DialogProgress, map_file: str, device: InputDevice) -> bool: ...
    def pair_host(self, dialog: DialogProgress) -> (str, str): ...
    def launch_game(self, game_id: str) -> None: ...
    def list_games(self) -> List[NvApp]: ...
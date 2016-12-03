from typing import Dict

from resources.lib.core.corefunctions import Core
from resources.lib.core.logger import Logger
from resources.lib.model.inputdevice import InputDevice
from resources.lib.storageengine.storage import TimedStorage


class InputRepository:
    storage = ... # type: TimedStorage
    logger = ... # type: Logger
    def __init__(self, core: Core, logger: Logger): ...
    def get_input_devices(self) -> Dict[InputDevice]: ...
    def add_input_device(self, device_id: str, device: InputDevice, flush=True) -> None: ...
    def remove_input_device(self, device_id: str, flush=True) -> None: ...
    def update_input_device(self, device_id: str, device: InputDevice, flush=True) -> None: ...
    def clear(self): ...

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union


class TTSaveABC(ABC):
    @abstractmethod
    def download(self) -> Optional[Dict[str, Union[str, List[str]]]]:
        pass


class UtilsABC(ABC):
    @abstractmethod
    def debug_out(self, message: str) -> None:
        pass

    @abstractmethod
    def clear_file_name(self, file_name: str) -> str:
        pass

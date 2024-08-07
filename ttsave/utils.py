import re
import colorama
from ttsave.abc import UtilsABC


class Utils(UtilsABC):
    def __init__(self, debug_mode: bool):
        self.debug_mode: bool = debug_mode

    def debug_out(self, message: str) -> None:
        if self.debug_mode:
            print(colorama.Fore.YELLOW + "[DEBUG] TTSave: " +
                  colorama.Fore.MAGENTA + message + colorama.Fore.RESET)

    def error_out(self, message: str) -> None:
        print(colorama.Fore.RED + "[ERROR] TTSave: " +
              colorama.Fore.LIGHTRED_EX + message + colorama.Fore.RESET)

    def clear_file_name(self, file_name: str) -> str:
        return re.sub(r'[\\/:*?"<>|] ',"", file_name).replace(" ", "_")

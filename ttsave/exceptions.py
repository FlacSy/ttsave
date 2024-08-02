from ttsave.utils import Utils

class _TTSaveError(Exception):
    """Базовый класс для всех кастомных ошибок TTSave."""
    def __init__(self, message: str, utils: Utils):
        self.message = message
        self.utils = utils
        self.utils.error_out(self.message)
        super().__init__(self.message)

class DriverInitializationError(_TTSaveError):
    """Ошибка инициализации веб-драйвера."""
    def __init__(self, message: str, utils: Utils):
        super().__init__(f"Ошибка инициализации веб-драйвера: {message}", utils)

class DownloadError(_TTSaveError):
    """Ошибка загрузки файла."""
    def __init__(self, file_name: str, message: str, utils: Utils):
        super().__init__(f"Ошибка загрузки файла: {file_name} - {message}", utils)

class URLNotProvidedError(_TTSaveError):
    """Ошибка: URL не был предоставлен."""
    def __init__(self, utils: Utils):
        super().__init__("URL не был предоставлен", utils)

class WebDriverNotInitializedError(_TTSaveError):
    """Ошибка: WebDriver не был инициализирован."""
    def __init__(self, utils: Utils):
        super().__init__("WebDriver не был инициализирован", utils)

class UnsupportedURLError(_TTSaveError):
    """Ошибка: Неподдерживаемый URL."""
    def __init__(self, url: str, utils: Utils):
        super().__init__(f"Неподдерживаемый URL: {url}", utils)

class VideoDownloadError(_TTSaveError):
    """Ошибка при загрузке видео."""
    def __init__(self, message: str, utils: Utils):
        super().__init__(f"Ошибка при загрузке видео: {message}", utils)

class PhotoDownloadError(_TTSaveError):
    """Ошибка при загрузке фото."""
    def __init__(self, message: str, utils: Utils):
        super().__init__(f"Ошибка при загрузке фото: {message}", utils)

class MusicDownloadError(_TTSaveError):
    """Ошибка при загрузке музыки."""
    def __init__(self, message: str, utils: Utils):
        super().__init__(f"Ошибка при загрузке музыки: {message}", utils)

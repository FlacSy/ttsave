import os
import logging
from ttsave import TTSave
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Инициализация TTSave
try:
    download_path = './downloads'
    tiktok_token = os.getenv('TT_CHAIN_TOKEN')
    
    if not tiktok_token:
        raise ValueError("Переменная окружения 'TT_CHAIN_TOKEN' не задана.")
    
    ttsave = TTSave(download_path, tiktok_token)
    logger.info("TTSave успешно инициализирован.")
except Exception as e:
    logger.error(f"Ошибка инициализации TTSave: {e}")
    exit(1)

# Список URL для скачивания
urls = [
    "https://www.tiktok.com/@example/video/1234567890",
    "https://www.tiktok.com/@example/video/0987654321",
    "https://www.tiktok.com/@example/video/1122334455",
]

# Скачивание видео из списка
for url in urls:
    try:
        logger.info(f"Скачивание видео: {url}")
        save_info = ttsave.save(url)
        if save_info:
            for file in save_info['files']:
                logger.info(f"Скачан файл: {file}")
        else:
            logger.warning(f"Не удалось скачать видео: {url}")
    except Exception as e:
        logger.error(f"Ошибка при скачивании {url}: {e}")

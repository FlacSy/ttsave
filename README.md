# TTSAVE - Скачивать ведь так просто 🫢

## Технологии

![Python](https://img.shields.io/badge/Python-3.10.0-blue)
![Node.js](https://img.shields.io/badge/Node.js-18.0.0-green)

![License](https://img.shields.io/github/license/FlacSy/ttsave)
![OS](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)

## Описание

TTSave упрощает процесс скачивания видео из TikTok, предоставляя удобный интерфейс для пользователей.

## Функционал TTSave
- Скачивание видео 
- Скачивание фото и аудио дорожки 

## Установка

1. Используйте pip для установки из [PyPi](https://pypi.org/project/ttsave/):

    ```bash
    pip3 install ttsave
    ```
2. Используйте pip + git для установки из [GitHub](https://github.com/FlacSy/ttsave/):

    ```bash
    pip3 install git+https://github.com/FlacSy/ttsave
    ```

## Требования
- Python 3.10.0 и выше 
- Node.js 18.0.0 и выше 

Библиотеки перечислены в файле [requirements.txt](./requirements.txt)

## Пример использования


```python
import os 
from ttsave import TTSave
from dotenv import load_dotenv

load_dotenv()

ttsave = TTSave('./downloads', os.getenv('TT_CHAIN_TOKEN'))

save_info = ttsave.save('TikTok url')

print(save_info)
```


## CLI

TTSave также предоставляет удобный интерфейс командной строки (CLI) для скачивания видео из TikTok. 

![cli](local/cli.png)

### Установка

CLI устанавливается вместе с библиотекой TTSave. Используйте одну из команд установки, приведенных выше.

### Примеры использования CLI

```bash
# Запуск CLI
ttsave

# Скачивание видео по URL
ttsave download <TikTok URL> <download_dir> --debug

# Показать версию
ttsave version

# Показать справку
ttsave help
```

### Команды CLI

- `download <url> <download_dir> <tt_chain_token>`: Скачивание видео или фото из TikTok по указанному URL. Параметр `download_dir` является необязательным, по умолчанию используется текущая директория, является обязательным, но после первого ввода сохраняеться как и директория `tt_chain_token` значения из cookies TikTok. Опция `--debug` включает режим отладки **на текущий момент опция недоступна**  

- `version`: Показать информацию о версии TTSave CLI.

- `help`: Показать доступные команды.

### FAQ

- #### Ничего не скачивается 
    Просто подождите и попробуйте позже. 
    **Также не забудте проверить ваш `tt_chain_token`!**

    Убедитесь, что все делаете по инструкции. 

    Если это не помогло, откройте issue на [GitHub](https://github.com/FlacSy/ttsave/issues).
    


> Если у вас возникли вопросы или проблемы, пожалуйста, откройте issue на [GitHub](https://github.com/FlacSy/ttsave/issues).
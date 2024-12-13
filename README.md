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
    pip3 install ttsave==2.0.0
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
from ttsave import TTSave

ttsave = TTSave('./downloads')

save_info = ttsave.save('https://www.tiktok.com/@example/video/1234567890')

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

- `download <url> <download_dir>`: Скачивание видео или фото из TikTok по указанному URL. Параметр `download_dir` является необязательным, по умолчанию используется текущая директория, но после первого ввода сохраняеться. Опция `--debug` включает режим отладки **на текущий момент опция недоступна**  

- `version`: Показать информацию о версии TTSave CLI.
- `exit`: Выйти из TTSave CLI.
- `help`: Показать доступные команды.

### FAQ

- #### Ничего не скачивается 
    Просто подождите и попробуйте позже. 
    **Также не забудте проверить ваш `tt_chain_token`!**

    Убедитесь, что все делаете по инструкции. 

    Если это не помогло, откройте issue на [GitHub](https://github.com/FlacSy/ttsave/issues).
    


> Если у вас возникли вопросы или проблемы, пожалуйста, откройте issue на [GitHub](https://github.com/FlacSy/ttsave/issues).

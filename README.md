# TTSAVE - Скачивать ведь так просто 🫢

**TTSave** - это Python библиотека для простого скачивания видео из `TikTok`.

## Технологии

![Python](https://img.shields.io/badge/Python-3.10.0-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.23.1-orange)

## Описание

TTSave упрощает процесс скачивания видео из TikTok, предоставляя удобный интерфейс для пользователей. Библиотека использует Selenium для автоматизации процесса скачивания, обеспечивая стабильность и надежность.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ttsave
```

## Требования

- Python 3.10.0
- Selenium 4.23.1
- Установленный Chrome браузер и ChromeDriver

## Пример использования

<details>
  <summary>Пример кода</summary>

```python
import os
from selenium import webdriver
from ttsave import Video

def main():
    url = "https://www.tiktok.com/@username/123321"
    options = webdriver.ChromeOptions()
    download_dir = f"{os.path.dirname(os.path.abspath(__file__))}/downloads"
    downloader = Video(
        url=url, 
        options=options,
        download_dir=download_dir
    )
    path = downloader.download()
    print(f"Downloaded file: {path}")

if __name__ == "__main__":
    main()
```

</details>

## Поддержка

Если у вас возникли вопросы или проблемы, пожалуйста, откройте issue на [GitHub](https://github.com/FlacSy/ttsave/issues).

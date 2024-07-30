import os
from selenium import webdriver
from ttsave import TTSave

def main():
    url = "https://www.tiktok.com/@flacsy.tw/photo/7298076877267242246"
    options = webdriver.ChromeOptions()
    download_dir = f"{os.path.dirname(os.path.abspath(__file__))}"
    downloader = TTSave(
        url=url,
        options=options,
        download_dir=download_dir,
        debug_mode=True
    )
    out = downloader.download()
    print(f"File(s): {out['files']}")
    print(f"Content type: {out['type']}")
    print(f"Content url: {out['url']}")

if __name__ == "__main__":
    main()

import os
from selenium import webdriver
from ttsave import TTSave
import time 

def main():
    url = input("TikTok URL: ")
    options = webdriver.FirefoxOptions()
    download_dir = os.path.dirname(os.path.abspath(__file__))
    
    downloader = TTSave(
        url=url,
        options=options,
        driver_class=webdriver.Firefox,
        download_dir=download_dir
    )
    start_time = time.time()
    out = downloader.download()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(out)
    downloader._quit_driver()
    
if __name__ == "__main__":
    main()
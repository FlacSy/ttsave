import os
import time
from selenium import webdriver
from ttsave import TTSave

def main():
    url = "https://www.tiktok.com/@flacsy.tw/photo/7298076877267242246"
    options = webdriver.FirefoxOptions()
    download_dir = os.path.dirname(os.path.abspath(__file__))
    
    downloader = TTSave(
        url=url,
        options=options,
        driver_class=webdriver.Firefox,
        driver_path=None,
        download_dir=download_dir,
        debug_mode=False
    )
    
    start_time = time.time() 

    out = downloader.download()
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"File(s): {out['files']}")
    print(f"Content type: {out['type']}")
    print(f"Content url: {out['url']}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()

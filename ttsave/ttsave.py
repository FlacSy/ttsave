import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Video:
    def __init__(self, url: str, options: webdriver.ChromeOptions, download_dir: str):
        self.url = url
        download_dir = download_dir
        prefs = {
            "download.default_directory": download_dir,               
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--mute-audio") 
        options.add_argument("--disable-dev-shm-usage") 

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)

    def _download_file(self, video_file_name: str):
        with open("./ttsave/scripts/download.js", "r", encoding="utf-8") as f:
            script = f.read()
        script = script.replace('video_file_name', video_file_name)
        self.driver.execute_script(script)   

    def download(self) -> str:
        if self.url is None:
            raise ValueError("URL is not provided")
        if not self.driver:
            raise ValueError("WebDriver is not initialized")
        
        return self._download_video()


    def _download_video(self) -> str: 
        try:
            video_element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )

            video_url = video_element.get_attribute("src")

            video_name_element = self.driver.find_element(By.XPATH, "//meta[@property='og:description']")
            video_file_name = f"{video_name_element.get_attribute('content')}.mp4"

            self.driver.get(video_url)
            self._download_file(video_file_name)
            return video_file_name
        finally:
            time.sleep(3)
            self.driver.quit()
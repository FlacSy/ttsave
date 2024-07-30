import os
import re
import requests
from typing import Dict, List, Optional, Type, Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ttsave.utils import Utils
from ttsave.ttsave_abc import TTSaveABC

class TTSave(TTSaveABC):
    def __init__(self, url: str, driver_path: str, driver_class: Type[webdriver.Chrome], options: webdriver.ChromeOptions, download_dir: str, debug_mode: bool = False):
        self.url: str = url
        self.download_dir: str = download_dir
        self.driver_path = driver_path
        self.debug_mode: bool = debug_mode

        self.utils: Utils = Utils(debug_mode=debug_mode)
        self.debug_out: callable = self.utils.debug_out
        self.clear_file_name: callable = self.utils.clear_file_name

        self.driver: Optional[webdriver.Chrome] = None
        self.wait: Optional[WebDriverWait] = None

        self.initialize_driver(driver_class, options)

    def initialize_driver(self, driver_class: Type[webdriver.Chrome], options: webdriver.ChromeOptions) -> None:
        if driver_class == webdriver.Chrome:
            prefs: Dict[str, str] = {
                "download.default_directory": self.download_dir,
            }
            options.add_experimental_option("prefs", prefs)
        if driver_class == webdriver.Firefox:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", self.download_dir)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4")         

        if not self.debug_mode:
            options.add_argument("--headless")
            
        options.add_argument("--no-sandbox")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-dev-shm-usage")
        
        self.driver = driver_class(options=options, service=self.driver_path)
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)
        self.debug_out("WebDriver initialized and page loaded.")
        self.debug_out("TTSave initialized.")

    def _download_file(self, video_file_name: str) -> None:
        with open("./ttsave/scripts/download.js", "r", encoding="utf-8") as f:
            script: str = f.read()
        script = script.replace('video_file_name', video_file_name)
        self.driver.execute_script(script)
        self.debug_out(f"Download script executed for file: {video_file_name}")

    def download(self) -> Optional[Dict[str, Union[str, List[str]]]]:
        if not self.url:
            raise ValueError("URL is not provided")
        if not self.driver:
            raise ValueError("WebDriver is not initialized")

        self.debug_out(f"Normalized URL: {self.url}")
        self.url = requests.get(self.url).url
        if re.match(r"https:\/\/www\.tiktok\.com\/@([a-zA-Z0-9_.]+)\/video\/([0-9]+)", self.url):
            return self._download_video()
        elif re.match(r"https:\/\/www\.tiktok\.com\/@([a-zA-Z0-9_.]+)\/photo\/([0-9]+)", self.url):
            return self._download_photo()
        else:
            self.debug_out("Unsupported URL")
            return None

    def _download_video(self) -> Dict[str, Union[str, List[str]]]:
        try:
            video_element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            video_url: str = video_element.get_attribute("src")
            self.debug_out(f"Video URL found: {video_url}")

            video_name_element = self.driver.find_element(
                By.XPATH, "//meta[@property='og:description']")
            video_file_name: str = f"{self.clear_file_name(video_name_element.get_attribute('content'))}.mp4"
            self.debug_out(f"Video file name: {video_file_name}")

            self.driver.get(video_url)
            self._download_file(video_file_name)
            output: Dict[str, Union[str, List[str]]] = {
                "type": "video",
                "files": [f"{self.download_dir}/{video_file_name}"],
                "url": self.url
            }
            self.debug_out(f"Video download completed: {video_file_name}")
            return output

        except Exception as e:
            self.debug_out(f"An error occurred while downloading video: {str(e)}")
            return None

    def _download_photo(self) -> Dict[str, Union[str, List[str]]]:
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//meta[@property='og:description']"))
            )
            name_element = self.driver.find_element(
                By.XPATH, "//meta[@property='og:description']")

            self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "css-brxox6-ImgPhotoSlide.e10jea832"))
            )
            photo_elements = self.driver.find_elements(
                By.CLASS_NAME, "css-brxox6-ImgPhotoSlide.e10jea832")

            files: List[str] = []
            seen_urls: set = set()

            for photo_element in photo_elements:
                photo_url: str = photo_element.get_attribute("src")
                if photo_url in seen_urls:
                    continue
                seen_urls.add(photo_url)

                index: int = len(seen_urls)
                photo_file_name: str = f"{index}_{self.clear_file_name(name_element.get_attribute('content'))}.jpg"
                self.debug_out(f"Downloading photo: {photo_file_name} from URL: {photo_url}")

                file_path: str = self._save_content(photo_url, photo_file_name)
                files.append(file_path)

            audio_element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "audio"))
            )
            audio_url: str = audio_element.get_attribute("src")
            audio_file_name: str = f"{self.clear_file_name(name_element.get_attribute('content'))}.mp3"
            self.debug_out(f"Downloading audio: {audio_file_name} from URL: {audio_url}")

            audio_file_path: str = self._save_content(audio_url, audio_file_name)
            files.append(audio_file_path)

            self.debug_out(f"Photo and audio download completed.")
            output: Dict[str, Union[str, List[str]]] = {
                "type": "photo",
                "files": files,
                "url": self.url
            }
            return output

        except Exception as e:
            self.debug_out(f"An error occurred while downloading photos: {str(e)}")
            return None

    def _save_content(self, url: str, file_name: str) -> str:
        response = requests.get(url)
        file_path: str = f"{self.download_dir}/{self.clear_file_name(file_name)}"
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(response.content)
            self.debug_out(f"File saved: {file_path}")
        else:
            self.debug_out(f"File already exists: {file_path}")
        return file_path

    def _quit_driver(self) -> None:
        if self.driver:
            self.driver.quit()
            self.debug_out("WebDriver quit.")
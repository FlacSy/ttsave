import os
import re
import time
import requests
from typing import Dict, List, Optional, Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ttsave.utils import Utils
from ttsave.ttsave_abc import TTSaveABC


class TTSave(TTSaveABC):
    def __init__(self, url: str, options: webdriver.ChromeOptions, download_dir: str, debug_mode: bool = False):
        self.url: str = url
        self.download_dir: str = download_dir
        self.debug_mode: bool = debug_mode
        prefs: Dict[str, str] = {
            "download.default_directory": download_dir,
        }
        options.add_experimental_option("prefs", prefs)
        if not debug_mode:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--mute-audio")
        options.add_argument("--disable-dev-shm-usage")
        self.utils: Utils = Utils(debug_mode=debug_mode)
        self.debug_out: callable = self.utils.debug_out
        self.clear_file_name: callable = self.utils.clear_file_name

        self.driver: webdriver.Chrome = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)
        self.debug_out("WebDriver initialized and page loaded.")

        self.debug_out("TTSave initialized.")

    def _download_file(self, video_file_name: str) -> None:
        with open("./ttsave/scripts/download.js", "r", encoding="utf-8") as f:
            script: str = f.read()
        script = script.replace('video_file_name', video_file_name)
        self.driver.execute_script(script)
        self.debug_out(f"Download script executed for file: {video_file_name}")

    def download(self) -> Optional[Dict[str, Union[str, List[str]]]]:
        if self.url is None:
            raise ValueError("URL is not provided")
        if not self.driver:
            raise ValueError("WebDriver is not initialized")
        self.url = requests.get(self.url).url
        self.debug_out(f"Normalized URL: {self.url}")
        if re.match(r"https:\/\/www\.tiktok\.com\/@([a-zA-Z0-9_.]+)\/video\/([0-9]+)", self.url):
            return self._download_video()
        elif re.match(r"https:\/\/www\.tiktok\.com\/@([a-zA-Z0-9_.]+)\/photo\/([0-9]+)", self.url):
            return self._download_photo()
        else:
            self.debug_out("Unsupported URL")
            raise ValueError("Unsupported URL")

    def _download_video(self) -> Dict[str, Union[str, List[str]]]:
        try:
            video_element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )
            video_url: str = video_element.get_attribute("src")
            self.debug_out(f"Video URL found: {video_url}")

            video_name_element = self.driver.find_element(
                By.XPATH, "//meta[@property='og:description']")
            video_file_name: str = f"{video_name_element.get_attribute('content')}.mp4"
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

        finally:
            time.sleep(3)
            self.driver.quit()

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
                photo_file_name: str = f"{index}_{name_element.get_attribute('content')}.jpg"
                self.debug_out(
                    f"Downloading photo: {photo_file_name} from URL: {photo_url}")

                response = requests.get(photo_url)
                file_path: str = f"{self.download_dir}/{self.clear_file_name(photo_file_name)}"

                if not os.path.exists(file_path):
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    files.append(file_path)
                else:
                    self.debug_out(f"File already exists: {file_path}")

            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "audio"))
            )
            audio_element = self.driver.find_element(By.TAG_NAME, "audio")
            audio_url: str = audio_element.get_attribute("src")
            audio_file_name: str = f"{name_element.get_attribute('content')}.mp3"
            self.debug_out(
                f"Downloading audio: {audio_file_name} from URL: {audio_url}")

            response = requests.get(audio_url)
            audio_file_path: str = f"{self.download_dir}/{self.clear_file_name(audio_file_name)}"

            if not os.path.exists(audio_file_path):
                with open(audio_file_path, "wb") as f:
                    f.write(response.content)
                files.append(audio_file_path)
            else:
                self.debug_out(f"Audio file already exists: {audio_file_path}")

            self.debug_out(
                f"Photo download completed. Audio file: {audio_file_name}")

            out: Dict[str, Union[str, List[str]]] = {
                "type": "photo",
                "files": files,
                "url": self.url
            }
            return out

        except Exception as e:
            self.debug_out(f"An error occurred: {str(e)}\n{e.__traceback__}")
        finally:
            time.sleep(3)
            self.driver.quit()

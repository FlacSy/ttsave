from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ttsave import TTSave

def download_video(download_dir: str, url: str):
    options = Options()
    
    ttsave = TTSave(
        driver_class=webdriver.Chrome,
        options=options,
        download_dir=download_dir,
        url=url
    )
    
    result = ttsave.download()
    if result:
        print("🎥 ~Video Download Result:~")
        print(f"~Type:~ {result.get('type')}")
        print(f"~Author Username:~ {result.get('author_username')}")
        print(f"~Files:~")
        for file in result.get('files', []):
            print(f"   - {file}")
        print(f"~URL:~ {result.get('url')}")
        print(f"~Music URI:~ {result.get('music_uri')}")
    else:
        print("⚠️ Failed to download video.")

def download_photo(download_dir: str, url: str):
    options = Options()

    ttsave = TTSave(
        driver_class=webdriver.Chrome,
        options=options,
        download_dir=download_dir,
        url=url
    )
    
    result = ttsave.download()
    if result:
        print("📸 ~Photo Download Result:~")
        print(f"~Type:~ {result.get('type')}")
        print(f"~Author Username:~ {result.get('author_username')}")
        print(f"~Files:~")
        for file in result.get('files', []):
            print(f"   - {file}")
        print(f"~URL:~ {result.get('url')}")
        print(f"~Music URI:~ {result.get('music_uri')}")
    else:
        print("⚠️ Failed to download photo.")

def download_music(download_dir: str, url: str):
    options = Options()

    ttsave = TTSave(
        driver_class=webdriver.Chrome,
        options=options,
        download_dir=download_dir,
        url=url
    )
    
    result = ttsave.download()
    if result:
        print("🎵 ~Music Download Result:~")
        print(f"~Type:~ {result.get('type')}")
        print(f"~Author:~ {result.get('author', {}).get('name')}")
        print(f"~Author URL:~ {result.get('author', {}).get('url')}")
        print(f"~Thumbnail URL:~ {result.get('thumb_url')}")
        print(f"~Clip Count:~ {result.get('clip_count')}")
        print(f"~Clips:~")
        for clip in result.get('clips', []):
            print(f"   - {clip}")
        print(f"~URL:~ {result.get('url')}")
    else:
        print("⚠️ Failed to download music.")

if __name__ == "__main__":
    download_dir = "./downloads"
    
    video_url = "https://www.tiktok.com/@username/video/123456789"
    print("\n--- Starting Video Download ---")
    download_video(download_dir, video_url)
    
    photo_url = "https://www.tiktok.com/@username/photo/123456789"
    print("\n--- Starting Photo Download ---")
    download_photo(download_dir, photo_url)
    
    music_url = "https://www.tiktok.com/music/trackname-123456"
    print("\n--- Starting Music Download ---")
    download_music(download_dir, music_url)

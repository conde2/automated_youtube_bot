import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from instaloader import instaloader
import config
import subprocess

def selenium_cookie_to_netscape(cookie):
    """
    Converts a Selenium cookie to Netscape format.
    """
    # Get the necessary cookie information
    name = cookie['name']
    value = cookie['value']
    domain = cookie['domain']
    path = cookie['path']
    expires = str(int(cookie['expiry']))
    secure = 'TRUE' if cookie['secure'] else 'FALSE'
    http_only = 'TRUE' if cookie['httpOnly'] else 'FALSE'

    # Create the Netscape cookie string
    netscape_cookie = f"{domain}\t{http_only}\t{path}\t{secure}\t{expires}\t{name}\t{value}"
    
    return netscape_cookie

def create_instagram_cookies():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en_US")
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe", chrome_options=options)
    driver.set_window_size(414, 896)
    driver.get(config.INSTAGRAM_URL)

    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    # clear the input boxes
    username.clear()
    password.clear()

    # input username and password
    username.send_keys(config.INSTAGRAM_USERNAME)
    password.send_keys(config.INSTAGRAM_PASSWORD) 

    # login button auto click
    log_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']"))).click()

    # Get all available cookies
    cookies = driver.get_cookies()
    netscape_cookies = [selenium_cookie_to_netscape(cookie) for cookie in cookies]

    # Write the cookies to a file in Netscape format
    with open(config.COOKIES_PATH, 'w') as f:
        f.write('# Netscape HTTP Cookie File\n')
        for cookie in netscape_cookies:
            f.write(cookie + '\n')

def scrape_instagram_videos(content):
    videos_directory = content.get("videos_path", config.VIDEOS_DIRECTORY + content.get("subject").lower() + "/")
    archive_path = content.get("archive_path", config.ARCHIVE_DIRECTORY + content.get("subject").lower() + ".db")
    urls_path = content.get("urls", config.URLS_DIRECTORY + content.get("subject").lower() + ".txt")
    cookies_path = content.get("cookies_path", config.COOKIES_PATH)

    print("Start scrapping")
    start_time = time.perf_counter()

    commands = ["gallery-dl", 
                    "--filter", "extension == 'mp4'",
                    "--filesize-max", config.INSTAGRAM_VIDEO_MAX_DOWNLOAD_SIZE,
                    "--cookies", cookies_path,
                    "--download-archive", archive_path,
                    "-D", videos_directory,
                    "-i", urls_path,
                ]

    commands_txt = " ".join(commands)
    print("Running command: " + commands_txt)
    subprocess.run(commands)
    end_time = time.perf_counter()
    print(f"Finished scrapping in {end_time - start_time} seconds")

if __name__ == "__main__":
    #create_instagram_cookies()
    scrape_instagram_videos(config.CONTENT_TABLE[1])
# Fully Automated Youtube Channel

Code to run a fully automated youtube that can scrape content, edit a compilation, and upload to youtube daily.
Based on this repository https://github.com/nathan-149/automated_youtube_channel/

# Instructions

1. [Download] The Github Repository

2. Download and install [Python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) if necessary.

3. Install libraries with `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt` .

4. Get setup and create a Project with the Youtube API: https://developers.google.com/youtube/v3/quickstart/python
Be sure to follow it carefully, as it won't work if you don't do this part right.
Download your OATH file and name it as "googleAPI.json" in your project folder.

6. Create an instagram account and follow accounts you want to scrape from

7. Open config.py in a text editor and fill in instagram credentials and openai token

- Note that you can edit variables inside config.py in a text editor and things such as:

```py
  INSTAGRAM_USERNAME = "" 
  INSTAGRAM_PASSWORD = ""
  VIDEO_MIN_DURATION = 5 * 60
  VIDEO_MAX_DURATION = 10 * 60
  CLIP_MIN_DURATION = 6
  CLIP_MAX_DURATION = 30
  INSTAGRAM_VIDEO_MAX_DOWNLOAD_SIZE = "15M"
  DAILY_SCHEDULED_TIME = "20:00"
  CHAT_GPT_API_KEY = ""
```

9. Run `python3 setup_google.py`

10. Run `python3 main.py` in your computer terminal (terminal or cmd). You have to sign in to your Youtube Account through the link the script will give you. It's going to ask you: "Please visit this URL to authorize this application:..." so you copy that link, paste it in your browser, and then sign into your Google account. Then paste the authentication code you get back into your terminal. It will then say "Starting Scraping" and sign into your instagram account.

11. Enjoy your fully automated youtube channel! :) Note that for uploading public videos, you have to complete an audit for the Youtube API. See the note in the [Google Documentation](https://developers.google.com/youtube/v3/docs/videos/insert). Without this, you can only post private videos, but they approve everyone. Have fun!

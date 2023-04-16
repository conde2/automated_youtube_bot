from scrape_videos import scrape_instagram_videos
from make_compilation import compile_video
from upload_video import upload_youtube_video
import schedule
import time
import datetime
import random
import config

def routine():
    print('[ Routine ] - Started at {date:%d/%m/%Y - %H:%M:%S}'.format(date=datetime.datetime.now()))

    random_content = random.choice(config.CONTENT_TABLE)
    output_file = ''
    for i in range(0, 2):
        # Try to make a compilation
        output_file = compile_video(random_content)
       
        # Try scrapping videos if compilation failed
        if (not output_file or output_file == ''):
            scrape_instagram_videos(random_content)
            print('[ Routine ] - Finished scrapping videos at {date:%d/%m/%Y - %H:%M:%S}'.format(date=datetime.datetime.now()))
        else:
            print('[ Routine ] - Compilation finished at {date:%d/%m/%Y - %H:%M:%S}'.format(date=datetime.datetime.now()))
            print("[ Routine ] - Finished generate file: " + output_file)
            break

    # Step 3: Upload to Youtube
    upload_youtube_video(content=random_content, output_file=output_file)

    print('[ Routine ] - Finished at {date:%d/%m/%Y - %H:%M:%S}'.format(date=datetime.datetime.now()))

def attemptRoutine():
    while(1):
        try:
            routine()
            break

        except OSError as err:
            print("Routine Failed on " + "OS error: {0}".format(err))
            time.sleep(60*60)

# Run routine every day at scheduled time
schedule.every().day.at(config.DAILY_SCHEDULED_TIME).do(attemptRoutine)

attemptRoutine()
while True:
    schedule.run_pending()  
    time.sleep(60) # wait one min


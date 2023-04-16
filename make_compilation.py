from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import os
from os.path import isfile, join
import random
import shutil
from collections import defaultdict
import hashlib
import config
import datetime

VideoFileClip.resize = resize

# makeCompilation takes videos in a folder and creates a compilation with max length max_length
def compile_video(content):
    path = content.get("videos_path", config.VIDEOS_DIRECTORY + content["subject"].lower() + "/")
    intro_name = content.get("video_intro_path", '')
    outro_name = content.get("video_outro_path", '')
    max_length = content.get("video_max_duration", config.VIDEO_MAX_DURATION)
    min_lenght = content.get("video_min_duration", config.VIDEO_MIN_DURATION)
    max_clip_length = content.get("clip_min_duration", config.CLIP_MAX_DURATION)
    min_clip_length = content.get("clip_min_duration", config.CLIP_MIN_DURATION)
    output_file = config.OUTPUT_DIRECTORY + content.get("subject", "Unknown_Subject") + '_{date:%d_%m_%Y_%H_%M_%S}'.format(date=datetime.datetime.now()) + ".mp4"
    audio_path = content.get("audio_path", None)

    if not os.path.exists(path):
        os.mkdir(path)

    all_used_paths = []
    all_videos = []
    hash_dict = {}
    total_length = 0

    for file_name in os.listdir(path):

        file_path = join(path, file_name)
        if isfile(file_path) and file_name.endswith(".mp4"):
            try:
                file = open(file_path, 'rb')
                data = file.read()
                file.close()
            except:
                print("[ Compiling ] - Failed to read file: " + file_name)
                continue

            hashValue = hashlib.md5(data).hexdigest()
            if hashValue in hash_dict:
                try:
                    print("[ Compiling ] - Removing duplicate: " + file_name + " (duplicate of " + hash_dict[hashValue] + ")")
                    os.remove(file_path)
                except:
                    print("[ Compiling ] - Failed to remove duplicate: " + file_name)
                continue

            hash_dict[hashValue] = file_name

            # Destination path
            clip = VideoFileClip(file_path)
            clip = clip.resize(width=1920)
            clip = clip.resize(height=1080)
            duration = clip.duration
            if duration <= max_clip_length and duration >= min_clip_length:
                all_videos.append(clip)
                total_length += duration
                all_used_paths.append(file_path)


    print("[ Compiling ] - Total clips: " + str(len(all_videos)))
    print("[ Compiling ] - Total length: " + str(total_length))

    random.shuffle(all_videos)

    duration = 0
    # Add intro vid
    videos = []
    if intro_name != '':
        intro_vid = VideoFileClip("./" + intro_name)
        videos.append(intro_vid)
        duration += intro_vid.duration

    # Create videos
    for clip in all_videos:
        duration += clip.duration
        videos.append(clip)
        if duration >= max_length:
            # Just make one video
            break

    # Add outro vid
    if outro_name != '':
        outro_vid = VideoFileClip("./" + outro_name)
        videos.append(outro_vid)
        duration += outro_vid.duration

    if duration < min_lenght:
        print("[ Compiling ] - Not enough clips to create compilation")
        return False

    final_clip = concatenate_videoclips(videos, method="compose")

    # Create compilation
    final_clip.write_videofile(
        output_file, threads=16, remove_temp=True, temp_audiofile=audio_path, codec="libx264", audio_codec="aac")

    
    for path in all_used_paths:
        print("[ Compiling ] - Cleaning used clips " + path)
        try:
            os.remove(path)
        except OSError as e:  ## if failed, report it back to the user ##
            print("[ Compiling ] - Error cleaning used clips: %s - %s." % (e.filename, e.strerror))

    return output_file

if __name__ == "__main__":
    compile_video(config.CONTENT_TABLE[0])

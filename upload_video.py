import datetime
from googleapiclient.http import MediaFileUpload
from google_api_auth import google_auth
from generate_texts import generate_youtube_title
import os
import config

def upload_youtube_video(content, output_file):
    print("[ Uploader ] - Uploading to Youtube...")

    google_api = google_auth()
    if not google_api:
        print("[ Uploader ] - Upload Failed! Google API not authenticated")
        return False

    title = generate_youtube_title(content)
    description = content.get('description', "Assista e se divirta com esse incrível video!") + config.DESCRIPTION_END_TEMPLATE
    tags = content.get('tags', [])

    request_body = {
        'snippet': {
            'categoryId': 23,
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(output_file, chunksize=-1, resumable=True)

    response_upload = google_api.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    """
    googleAPI.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()
    """

    print("[ Uploader ] - Upload Successful! Video ID: " + response_upload.get('id'))

    # Step 4: Cleanup
    try:
        os.remove(output_file)
        print("Removed temp files!")
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))

    return True

if __name__ == "__main__":
    upload_youtube_video(config.CONTENT_TABLE[0], config.OUTPUT_DIRECTORY + "output.mp4")
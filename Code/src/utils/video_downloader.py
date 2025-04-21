import yt_dlp
import os
from pytube import YouTube
from src.constants import MP4_SUFFIX, MP4_INPUT_DIR
from src.constants import YOUTUBE_DIR

class VideoDownloader:
    def __init__(self):
        try:
            # Create directories if they don't exist
            os.makedirs(MP4_INPUT_DIR)
        except OSError as e:
            if os.path.isdir(MP4_INPUT_DIR):  # Handles existing folder case
                print(f"Folder '{MP4_INPUT_DIR}' already exists.")
            else:
                print(f"Error creating folder: {e}")

    def download_video_yt_dlp(self, youtube_id):
        """
        Downloads a video from YouTube by its unique identifier using yt_plp library and save it to your device
        Args:
            youtube_id (str): Identifier of video on YouTube
        """
        if not os.path.exists(MP4_INPUT_DIR):
            os.makedirs(MP4_INPUT_DIR)
        output_path = os.path.join(MP4_INPUT_DIR, youtube_id + MP4_SUFFIX)

        # Ensure that we only download video at most once.
        if os.path.exists(output_path):
            return

        video_url = YOUTUBE_DIR + youtube_id
        ydl_opts = {
            'outtmpl': output_path,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([video_url])
                print('Video was downloaded successfully using yt_plp library')
            except yt_dlp.DownloadError as e:
                print('Error downloading video:', e)

    def get_video_title(self, video_id):
        """
        Get the title of a video from a given URL
        Args:
            video_url (str): URL of the video
        Returns:
            str: Title of the video
        """
        video_url = YOUTUBE_DIR + video_id  
        ydl_opts = {
        'quiet': True,  # Suppress output
        'force_generic_extractor': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
        return info.get('title', 'No title found')
    
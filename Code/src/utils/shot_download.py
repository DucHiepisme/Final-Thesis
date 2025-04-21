import yt_dlp
import os
from pytube import YouTube
import subprocess
from src.constants import MP4_SUFFIX, SHORT_INPUT_DIR
from src.constants import YOUTUBE_DIR

class ShotDownloader:
    def __init__(self):
        try:
            # Create directories if they don't exist
            os.makedirs(SHORT_INPUT_DIR)
        except OSError as e:
            if os.path.isdir(SHORT_INPUT_DIR):  # Handles existing folder case
                print(f"Folder '{SHORT_INPUT_DIR}' already exists.")
            else:
                print(f"Error creating folder: {e}")

    def download_shot(self, youtube_id, start_time, end_time):
        """
        Downloads a video from YouTube by its unique identifier using yt_plp library and save it to your device
        Args:
            youtube_id (str): Identifier of video on YouTube
        """
        start_time_seconds = self.__convert_time(start_time)
        end_time_seconds = self.__convert_time(end_time)
        if not os.path.exists(SHORT_INPUT_DIR):
            os.makedirs(SHORT_INPUT_DIR)
        output_path = os.path.join(SHORT_INPUT_DIR, youtube_id + "_" + str(start_time_seconds) + "_" + str(end_time_seconds) + MP4_SUFFIX)

        # Ensure that we only download video at most once.
        if os.path.exists(output_path):
            return

        video_url = YOUTUBE_DIR + youtube_id
        command = [
            'yt-dlp', 
            '-o', output_path,
            '--postprocessor-args', 
            f'-ss {start_time_seconds} -to {end_time_seconds}', 
            video_url
        ]
        
        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"Video segment downloaded as: {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while downloading: {e}")

    def __convert_time(self, time_str):
        if ":" in time_str:
            minutes, seconds = map(int, time_str.split(':'))
            return minutes * 60 + seconds
        else:
            return int(time_str)

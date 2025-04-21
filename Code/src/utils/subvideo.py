from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import imageio
import moviepy as mpe
from moviepy.editor import VideoFileClip
from .video_downloader import VideoDownloader
from src.constants import MP4_INPUT_DIR, MP4_OUTPUT_DIR, MP4_SUFFIX, RESULT_DIR, CACHE_DIR


class SubVideo:
    def __init__(self):

        if not os.path.exists(RESULT_DIR):
            os.makedirs(RESULT_DIR)

        output_path = os.path.join(RESULT_DIR, MP4_OUTPUT_DIR)
        try:
            os.makedirs(output_path)  # Creates directories if they don't exist
        except OSError as e:
            if os.path.isdir(output_path):  # Handles existing folder case
                print(f"Folder '{output_path}' already exists.")
            else:
                print(f"Error creating folder: {e}")


    def cut_one_video(self, youtube_id, start_time, end_time):
        """
        Cuts a video from a specified start time to end time and saves it to a new file.
        Args:
            input_path (str): Path to the input video file.
            start_time (float): Start time in seconds.
            end_time (float): End time in seconds.
            output_path (str): Path to save the cut video file.
        """
        start_time_seconds = self.__convert_to_seconds(start_time)
        end_time_seconds = self.__convert_to_seconds(end_time)
        input_path = self.__get_input_path(youtube_id)
        with VideoFileClip(input_path) as video:
            cut_video = video.subclip(start_time_seconds, end_time_seconds)
            output_path = self.__create_output_path(youtube_id, start_time_seconds, end_time_seconds)
            cut_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    def __convert_to_seconds(self, time) -> int:
        minutes, seconds = time.split(':')
        seconds = int(minutes) * 60 + int(seconds)
        return seconds

    def __get_input_path(self, youtube_id) -> str:
        return os.path.join(MP4_INPUT_DIR, youtube_id + MP4_SUFFIX)

    def __create_output_path(self, youtube_id, start_time_seconds, end_time_seconds) -> str:
        return os.path.join(RESULT_DIR, MP4_OUTPUT_DIR, youtube_id + str(start_time_seconds) + '-' + str(end_time_seconds) + MP4_SUFFIX)

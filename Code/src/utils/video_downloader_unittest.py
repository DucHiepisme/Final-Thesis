import unittest
import os
import shutil
from src.utils.video_downloader import VideoDownloader
from src.constants import MP4_INPUT_DIR, MP4_SUFFIX


class VideoDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        try:
            # Creates directories if they don't exist
            os.makedirs(MP4_INPUT_DIR)
        except OSError as e:
            if os.path.isdir(MP4_INPUT_DIR):  # Handles existing folder case
                print(f"Folder '{MP4_INPUT_DIR}' already exists.")
            else:
                print(f"Error creating folder: {e}")

    def tearDown(self):
        shutil.rmtree(MP4_INPUT_DIR)

    def test_download_video_yt_dlp(self):
        youtube_id = "eBYY29GyAMM"
        expected_output_file = os.path.join(
            MP4_INPUT_DIR, youtube_id + MP4_SUFFIX)
        video_downloader = VideoDownloader()
        video_downloader.download_video_yt_dlp(youtube_id)
        self.assertTrue(os.path.exists(expected_output_file),
                        f"File not found at: {expected_output_file}")

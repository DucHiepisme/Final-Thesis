import os
import json
from src.utils.shot_download import ShotDownloader
from src.utils.video_downloader import VideoDownloader
from src.utils.subvideo import SubVideo
class ShotCreation:
    def __init__(self):
        """Initialize the JsonFileReader with the path to the folder containing JSON files."""
        self.json_data = []
        self.shot_downloader = ShotDownloader()
        self.video_downloader = VideoDownloader()
        self.sub_video = SubVideo()

    def read_folder(self, folder_path):
        self.folder_path = folder_path
        """Read all JSON files in the specified folder and store their data."""
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.json'):  # Check if the file is a JSON file
                file_path = os.path.join(self.folder_path, filename)  # Get the complete file path
                with open(file_path, 'r') as f:  # Open the file for reading
                    try:
                        data = json.load(f)  # Load the JSON data
                        name_without_extension = os.path.splitext(filename)[0]
                        for foul in data["fouls"]:
                            start_time = foul["start"]
                            end_time = foul["end"]
                            self.sub_video.cut_one_video(name_without_extension, start_time, end_time)
                        print("/n")
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file: {filename}")

    
   
    
  
import time
import openai
import timeit
from src.utils.infor_extraction import Infor_Extractor
from src.preprocess.subtitles_preprocess import Transcript
from src.preprocess.foul_moment_extraction import Foul_Extractor
from src.utils.shot_download import ShotDownloader
from src.preprocess.shot_creation import ShotCreation
from src.utils.video_downloader import VideoDownloader
from src.utils.subvideo import SubVideo
from src.preprocess.frame_collector import FrameCollector
import os
import json
# Example usage
# ex = Infor_Extractor()
# video_title = "GOAL | Boly O.G | Exeter City 2-2 Nottingham Forest | Fourth Round | Emirates FA Cup 2024-25"
# match_info = ex.foul_extraction()
# print(match_info)

# trans = Transcript()
# tranx = trans.get_transcript("rSE2YPcv89U")
# print(tranx)
folder_path = 'D:/Final Thesis/Code/result/video'  # Replace with your folder path
# json_reader = ShotCreation()
# json_rea
# down = VideoDownloader()
# down.download_video_yt_dlp("zUTUA0TKvfQ")

# sub = SubVideo()
# sub.cut_one_video("zUTUA0TKvfQ", "45:26", "45:37")

fr = FrameCollector()

fr.get_frame(folder_path)
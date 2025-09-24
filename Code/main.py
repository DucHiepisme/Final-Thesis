import time
import openai
from PIL import Image
import timeit
from src.utils.infor_extraction import Infor_Extractor
from src.preprocess.subtitles_preprocess import Transcript
from src.preprocess.foul_moment_extraction import Foul_Extractor
from src.utils.shot_download import ShotDownloader
from src.preprocess.shot_creation import ShotCreation
from src.utils.video_downloader import VideoDownloader
from src.utils.subvideo import SubVideo
from src.preprocess.unzip_data import DataProcessor
from src.workflow.eval_text_classifier import TextEvaluation
from src.workflow.frame_classification import FrameClassifier
from src.workflow.subtitle_process import SubtitleExtractor
from src.workflow.workflow import Workflow
import os
import json
from src.constants import JSON_SUFFIX


if __name__ == "__main__":
    # Example usage - replace with your specific file
    file = "WZ9WQURYBTY_5947-5954_5962-5967"
    work = Workflow(file)
    work.run(file)

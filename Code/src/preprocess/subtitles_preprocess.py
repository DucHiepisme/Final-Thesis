from youtube_transcript_api import YouTubeTranscriptApi
import os
from src.constants import CACHE_DIR, SUBTITLES_DIR, SUMMARIES_DIR, JSON_SUFFIX
import json

class Transcript: 
    def __init__(self):
        try:
            os.makedirs(os.path.join(CACHE_DIR, SUBTITLES_DIR))
        except OSError as e:
            pass
    def get_transcript(self, video_id):
        """
        Get the transcript of a video from a given URL
        Args:
            youtube_id (str): Identifier of video on YouTube
        Returns:
            list: Transcript of the video
        """
        subs_path = os.path.join(CACHE_DIR, SUBTITLES_DIR, video_id + JSON_SUFFIX)
        if os.path.exists(subs_path):
            with open(subs_path, "r") as f:
                imported_subs = json.load(f)
                return imported_subs["subtitles"]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','es','vi'])
            text = [item['text'] for item in transcript]
            start = [item['start'] for item in transcript]
            transcript_dict = {}

            for i in range(len(text)):
                minutes = int(start[i]) // 60
                seconds = int(start[i]) % 60
                minute_start = f"{minutes:02d}:{seconds:02d}"
                transcript_dict[minute_start] = text[i]

            with open(subs_path, "w", encoding="utf-8") as f:
                json.dump({"subtitles": transcript_dict}, f, ensure_ascii=False)

            return transcript_dict
        except Exception:
            pass
    
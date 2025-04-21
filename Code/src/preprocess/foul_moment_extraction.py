import openai
from src.constants import OPEN_AI_API_KEY
import yaml
import os
import json
import time
from src.preprocess.subtitles_preprocess import Transcript
from src.constants import CACHE_DIR, SUBTITLES_DIR, JSON_SUFFIX
class Foul_Extractor:
    def __init__(self):
        api_key = OPEN_AI_API_KEY
        self.api_key = api_key
        openai.api_key = self.api_key
        config_file = "./config/prompt.yml"

        self.config = None
        with open(config_file, "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)
    def extract_foul_info(self, video_id):
        text = self.__get_transcription(video_id)
        segment = self.segment_text(text)

        #Run each segment through the model
        for s in segment:    
        #Setting up the prompt
            prompt = self.config["PROMPT"].format(s)
            extracted_info = ""
            while True:
                try:
                    # Call the OpenAI API with updated structure
                    response = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {
                                "role": "system",
                                "content": "Extract information about fouls from the match subtitles."
                            },
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ],
                        max_tokens=4000
                    )
                    break
                except Exception as e:
                    print(f"Rate limit exceeded or other error: {str(e)}. Retrying in 5 seconds...")
                    time.sleep(5)
            if response.choices and response.choices[0].message:
                extracted_info += response.choices[0].message.content
                print(response.choices[0].message.content)
        return extracted_info
        
       

    def segment_text(self, timestamp: dict) -> list[str]:
        '''
        Segments the input into smaller chunks to fit PALM'API
        Input:
            timestamp : {
                "timestamp": "text",
                "timestamp": "text",
                "timestamp": "text",
            }

        Output is a list of str:
            [
            "timestamp => text\n"timestamp => text\n"timestamp => text"
            ......
            "timestamp => text\n"timestamp => text\n"timestamp => text"
            ]
        '''
        text = ""
        for k, v in timestamp.items():
            text = text + k + " => " + v + "\n"

        timestamps = text.split("\n")
        texts = []

        temp = 1

        t = ""
        for ti in timestamps:
            if len(ti) == 0:
                continue

            x = ti[:ti.find(":")]

            x = int(x)
            if x % 10 == 1 and x > 1:

                if temp != x:
                    texts.append(t)
                    t = ti
                    temp = x
                else:
                    t = t + "\n" + ti
            else:
                t = t + "\n" + ti

        texts.append(t)

        return texts
    def __get_transcription(self, video_id):
        path = os.path.join(CACHE_DIR, SUBTITLES_DIR, video_id + JSON_SUFFIX)
        try:
            with open(path,'r', encoding='utf-8') as file:
                data = json.load(file)
                return data["subtitles"]
        except FileNotFoundError:
            print(f"File not found. Running subtitle_crawl.py...")
            self.__run_get_transcription(video_id)
            with open(path, "r", encoding='utf-8') as file:
                data = json.load(file)
                return data["subtitles"]    


    def __get_scoring_timestamps(self, transcripts):
        texts = self.segment_text(transcripts)

    def __run_get_transcription(self, video_id):
        collect = Transcript()
        return collect.get_transcript(video_id)
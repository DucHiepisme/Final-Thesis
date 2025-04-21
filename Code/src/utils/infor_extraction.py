import time
import openai
from src.constants import OPEN_AI_API_KEY
import yaml
class Infor_Extractor:
    def __init__(self):
        api_key = OPEN_AI_API_KEY
        self.api_key = api_key
        openai.api_key = self.api_key
        config_file = "./config/prompt.yml"

        self.config = None
        with open(config_file, "r") as ymlfile:
            self.config = yaml.safe_load(ymlfile)

    def extract_match_info(self, title):    
    # Prepare the prompt
        prompt = f"Extract the following information from the title: '{title}'.\n" \
             f"Information required: league, nation, home team, away team, full year."

    # Retry mechanism for rate limit errors
        while True:
            try:
                # Call the OpenAI API with updated structure
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "Extract match information from the title."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=200
                )
                break
            except Exception as e:
                print(f"Rate limit exceeded or other error: {str(e)}. Retrying in 5 seconds...")
                time.sleep(5)

        # Get the response text
        if response.choices and response.choices[0].message:
            extracted_info = response.choices[0].message.content
            return extracted_info
        return None
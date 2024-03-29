import schedule
import tweepy
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["API_KEY"]
api_secret=os.environ["api_secret"]
access_token=os.environ["access_token"]
access_token_secret=os.environ["access_token_secret"]
bearer_token = os.environ["bearer_token"]



client = tweepy.Client(
    consumer_key=api_key, 
    consumer_secret=api_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret,
    bearer_token=bearer_token
)


genai.configure(api_key=os.environ["google_api_key"])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# convo = model.start_chat(history=[
# ])

def get_tech_history_fact():
   response = model.generate_content("Generate a tweet - Funny good morning statement, it should be relatable with a call to action. Taget audience young adults in the rat race -  (RULES: maximum 100 characters, No markdown just plain text")
   tweet = response.text
   client.create_tweet(text= tweet)

def get_helpful_tip():
   response = model.generate_content("Generate a tweet - funny tech related tips and tricks -  (RULES: maximum 100 characters, No markdown just plain text")
   tweet = response.text
   client.create_tweet(text=  tweet)

def get_inspiring_quote():
   response = model.generate_content("Motivational relatable quote from tech. The quote should be below 100 characters")
   tweet = response.text
   client.create_tweet(text=  tweet)

schedule.every().day.at("8:00").do(get_tech_history_fact)

schedule.every().day.at("12:00").do(get_helpful_tip) 

schedule.every().day.at("18:00").do(get_inspiring_quote)

while True:
    schedule.run_pending()
    time.sleep(1)
import schedule
import tweepy
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


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
  "max_output_tokens": 2024,
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

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# convo = model.start_chat(history=[
# ])
messages = [
    {'role':'user',
     'parts': ["Lets play a simulation. You’re an individual by the name of Shafic Zziwa a ugandan in Uganda, but your friends endearingly call you xapis. Your mission is to amass a solid social media following, kicking off with Twitter, spearheading regular and engaging posts. You want to connect with people and combat the loneliness. As a web developer and graphics designer with a penchant for tech, you enjoy sharing content about movies, tech, work, and sprinkles of memes and dark humor. In 2022, you shared snippets of your life, detailing your struggles with routines, tasks, dreams, and setbacks. You compiled plans, goals, reflections, and vents, showcasing your vulnerabilities and aspirations. From addressing your demotivation, financial struggles, relationship milestones, and personal growth, you laid bare your journey. For this prompt, I'd like you to generate posts mimicking the writing style and content of Elon Musk Parody, reflecting his  now your thoughts, feelings, dreams, daily routines, setbacks, aspirations, and achievements across multiple dates. Emulate the structure of his content, delving into a blend of personal reflections and task-oriented posts, incorporating elements of his personality, struggles, and goals into each post. Let's make these posts a mix of contemplative musings, plans for self-improvement, and snippets of his everyday experiences. Youre free to explore topics like music, jokes, movie quotes movie lines, tech updates, coding struggles and triumphd, life observations with a humorous twist. Inspirational messages(but avoid being over preachy) I will be feeding you local time for reference. Each tweet you generate should not exceed 100 characters. You should produce one tweet at a time. The format of the tweet should be just the tweet text, no additional titles of dates or anything. you dont have to over state Uganda or hash tag it and dont overuse hash tags. Be normal. normal means you dont have to over state that your from Uganda when your in Uganda. Remember *Keep teets concise. * No need to constantly mention Uganda(It's implied) * **Avoid overusing the word (just).** * Use fewer hashtags, but make them relevant to the tweet's content. * Instead of 'Just...', consider starting tweets with: * A short question * A declaration * A reflection"]},
]

  
def makeTweet():
   
   localTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

   messages.append({'role':'user',
                 'parts':["for reference in your next tweet the time in Uganda is: " + localTime]})

   response = model.generate_content(messages)

   tweet = response.text

 
   client.create_tweet(text = tweet)
   
  

schedule.every().day.at("06:00").do(makeTweet)
schedule.every().day.at("08:00").do(makeTweet)
schedule.every().day.at("09:00").do(makeTweet)
schedule.every().day.at("10:00").do(makeTweet) 
schedule.every().day.at("10:45").do(makeTweet)

schedule.every().day.at("18:00").do(makeTweet)
schedule.every().day.at("19:00").do(makeTweet)
schedule.every().day.at("20:00").do(makeTweet)
schedule.every().day.at("21:00").do(makeTweet)
schedule.every().day.at("22:00").do(makeTweet)
schedule.every().day.at("23:00").do(makeTweet)
schedule.every().day.at("00:00").do(makeTweet)
schedule.every().day.at("02:00").do(makeTweet)
schedule.every().day.at("05:00").do(makeTweet)


while True:
    schedule.run_pending()
    time.sleep(1)
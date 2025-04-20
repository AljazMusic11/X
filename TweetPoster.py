import tweepy
import os
import openai
import random
from dotenv import load_dotenv

load_dotenv(dotenv_path="APIs.env")

openai.api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

system_message = {
    "role": "system", 
    "content": "You are a helpful assistant who writes short, high-quality, tweet-length content tailored to the user's request. Stay clear, concise, and impactful. Do not use emojis unless asked."
}

def load_prompts(file_path="prompts.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [{"role": "user", "content": line.strip()} for line in lines if line.strip()]

prompts = load_prompts()

selected_prompt = random.choice(prompts)

response = openai.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4"
    messages=[system_message, selected_prompt],
    max_tokens=60  # Limit tweet length
)

def post_tweet():

    tweet = response.choices[0].message.content
    client.create_tweet(text=tweet)
    print(f"Posted: {tweet}")

post_tweet()

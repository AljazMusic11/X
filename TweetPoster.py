import tweepy
import os
import openai
import random
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

system_message = {
    "role": "system", 
    "content": "You are a motivational coach who provides discipline, self-improvement, and personal growth advice. Write short, tweet-length motivational messages. Your tone should be empowering, direct, and action-oriented."
}

# Define different user prompts for varied tweet content
prompts = [
    {"role": "user", "content": "Write a motivating tweet about hard work, god and discipline. Max 80 characters. Don't use emojis."},
    {"role": "user", "content": "Write a encouraging people to overcome their fears and take action. Max 80 characters. Don't use emojis."},
    {"role": "user", "content": "Write a very short (max 20 characters) motivating tweet with a very deep message. Don't use emojis."},
    {"role": "user", "content": "Write a motivating tweet numbering 3-5 things about god, discipline or hardwork. Start with very short (2-3 words) summary of what you listed. Don't use emojis."},
    {"role": "user", "content": "Write a motivating tweet about going to gym, working hard. Max 80 characters. Don't use emojis."}
]

# Randomly select one prompt from the list
selected_prompt = random.choice(prompts)

# Generate a response for the selected prompt
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

import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None

GIPHY_API_KEY = "TyWj6PRSeLqIBw7OgCpuz4VjFZDUZTQY" 
USER_ID = "61353690"

def search_gif(keyword):
    endpoint = "https://api.giphy.com/v1/gifs/search"
    params = {"api_key": GIPHY_API_KEY, "q": keyword, "limit": 1,}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()

    gif_data = response.json().get("data", [])
    if gif_data:
        return gif_data[0].get("images", {}).get("original", {}).get("url", "")

def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []

def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    sender_id = message["sender_id"]
    sender_type = message["sender_type"]
    sender_name = message["name"]
    text = message["text"].lower()

    if sender_type == "user":
        if sender_id == USER_ID:
            send_message("Sup!")
        if "good morning" in text:
            send_message(f"Good morning, {sender_name}!")
        if "good night" in text:
            send_message(f"Good night, {sender_name}!")
        if "hi bot gif " in text:
            keyword = text.split("gif ", 1)[-1].strip()
            
            gif_url = search_gif(keyword)

            if gif_url:
                send_message(gif_url)
            else:
                send_message("Sorry, I can't find a GIF for the keyword.")
                
    LAST_MESSAGE_ID = message["id"]

def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()

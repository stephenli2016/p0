# GroupMe Bot User Guide

## Overview

- A GroupMe bot that will be able to read/respond to specfic messages in a GroupMe chat

## Features

1. Respond to only one user with the USER_ID in bot.py
  - The bot will respond to you and **only you** with text "Sup!" when seeing you text a message in the GroupMe chat, and if someone else sends the same message, **even with the same name**, your bot will not respond to them
 
2. good morning/good night
  - if *anyone* says good morning/good night, the bot will respond with a good morning/good night with their name
    - i.e. if someone says "good morning", the bot should respond with "good morning, <name>"
   
3. Search and reply a gif with the keyword that users provide
  - it uses Giphy's API (i.e. [Giphy](https://developers.giphy.com/docs/api/endpoint#search))
  - it will reply only with the following format "hi bot gif <keyword>"

## Running

```bash
# clone the repo to your local machine and cd into it 
git clone https://github.com/stephenli2016/p0.git && cd p0

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

# install dependencies
pip install -r requirements.txt

# run bot
python3 bot.py
```
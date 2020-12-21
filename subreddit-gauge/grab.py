#! python3
# Uses praw to pull data about subreddits.

import praw
import numpy as np
from secrets import client_id, client_secret, reddit_password

# praw object
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=f'Windows:{client_id}:v0.0.1 (by u/Free_Brandon)',
    username="Free_brandon",
    password=reddit_password,
)

subreddit = "learnpython"
#! python3
# Uses praw to pull data about subreddits.

import praw
import numpy as np
from secrets import client_id, client_secret, reddit_password

# praw object
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=f"Windows:{client_id}:v0.0.1 (by u/Free_Brandon)",
    username="Free_brandon",
    password=reddit_password,
)


def get_subscribers(subreddit_):
    """Gets current sub count.

    Inputs
    -------
    str: Desired subreddit name

    Returns
    -------
    int: sub count
    """
    subreddit = reddit.subreddit(subreddit_)
    return subreddit.subscribers()


def get_active(subreddit_):
    """Gets amount of users actively on subreddit.

    Inputs
    -------
    str: Desired subreddit name

    Returns
    -------
    int: Currently online user count.
    """
    subreddit = reddit.subreddit(subreddit_)
    return subreddit.active_user_count


def get_posts(subreddit_):
    """Gets amount of comments posted within last hour.

    Inputs
    -----
    str: Desired subreddit name.

    Returns
    ------
    int: len(comments)
    """
    subreddit = reddit.subreddit(subreddit_)
    posts = set()
    for submission in subreddit.top(time_filter="hour", limit=None):
        posts.add(submission)
    return len(posts)


print(get_posts("learnpython"))
print(get_active("learnpython"))

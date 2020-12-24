#! python3
# Uses praw to pull data about subreddits.

import praw
from credentials import (
    client_id,
    client_secret,
    reddit_password,
    useragent,
    reddit_username,
)

# praw object
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=useragent,
    username=reddit_username,
    password=reddit_password,
)


def get_subscribers(subreddit_, *args):
    """Gets current sub count for one or more subreddits.

    Inputs
    -------
    str: Desired subreddit name(s)

    Returns
    -------
    int: sub count or dict:{subreddit: int(sub count)}
    """
    if len(args) > 0:
        subreddit = reddit.subreddit(subreddit_)
        subcount = {subreddit_: subreddit.subscribers}
        for page in args:
            subreddit = reddit.subreddit(page)
            subcount[page] = subreddit.subscribers
        return subcount
    else:
        subreddit = reddit.subreddit(subreddit_)
        return subreddit.subscribers


def get_active(subreddit_, *args):
    """Gets amount of users actively on subreddit.

    Inputs
    -------
    str: Desired subreddit name(s)

    Returns
    -------
    int: Currently online user count or dict:{subreddit: int(active user count)}
    """
    if len(args) > 0:
        subreddit = reddit.subreddit(subreddit_)
        usercounts = {subreddit_: subreddit.subscribers}
        for page in args:
            subreddit = reddit.subreddit(page)
            usercounts[page] = subreddit.active_user_count
        return usercounts
    else:
        subreddit = reddit.subreddit(subreddit_)
        subreddit._fetch()
        return subreddit.active_user_count


def get_posts(subreddit_):
    """Gets amount of posts within last hour, upvotes, and number of comments.
    Inputs
    -----
    str: Desired subreddit name.

    Returns
    ------
    dict: {'submission(id)': ['score','len(comments)']}
    """
    subreddit = reddit.subreddit(subreddit_)
    posts = dict()
    for submission in subreddit.top(time_filter="hour", limit=None):
        score = submission.score
        posts[submission.id] = [score, len(submission.comments.list())]
    return posts
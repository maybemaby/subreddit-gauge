#! python3
# subreddit-gauge has functions to scrape info about a subreddit's hourly active users,
# subscribers, posts, and comments.That data is then put into pandas dataframes to be
# tracked over csv and eventually plotted.

from grab import get_active, get_subscribers, get_posts
import datetime, time
import pandas as pd
import numpy as np
from pathlib import Path

path = r"C:/Users/BrandonMa/Python projects/subreddit-gauge/"


def main():
    timeindex = []
    data = []
    postdata = {}
    for _ in range(24):
        hourly_posts = get_posts("learnpython")
        upvotes = 0
        for v in hourly_posts.values():
            upvotes += v[0]
        t = datetime.datetime.now()
        timeindex.append(t.strftime("%c"))
        data.append(
            [
                get_subscribers("learnpython"),
                get_active("learnpython"),
                len(hourly_posts),
                upvotes,
            ]
        )
        if postdata == None:
            postdata = hourly_posts
        else:
            postdata = postdata.update(hourly_posts)
        time.sleep(10)
    array1 = np.array(data)
    dti = pd.DatetimeIndex(timeindex)
    df = pd.DataFrame(
        array1,
        index=dti,
        columns=["Subs", "Active users", "Posts/hour", "Post upvotes/hour"],
    )
    df2 = pd.DataFrame.from_dict(
        postdata, orient="index", columns=["Scores", "Number of Comments"]
    )
    return df, df2


subreddit_data = main()
for i, df in enumerate(subreddit_data):
    filename = "learnpythondata" + str(i) + ".csv"
    existing_file = Path(path + filename)
    if existing_file.is_file():
        df.to_csv(filename, mode="a", header=False)
    else:
        df.to_csv(path_or_buf=path + filename)

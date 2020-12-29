#! python3
# subreddit-gauge has functions to scrape info about a subreddit's hourly active users,
# subscribers, posts, and comments.That data is then put into pandas dataframes to be
# tracked over csv and eventually plotted.

from grab import get_active, get_subscribers, get_posts
from plots import plot_activity, plot_users_vs_tod, plot_users_vs_act
import datetime
import pandas as pd
import numpy as np
from pathlib import Path

path = Path.home() / "Python projects" / "subreddit-gauge"

# Run the file to collect the data then print the graphs.
def main(subreddit):
    timeindex = []
    data = []
    postdata = {}
    for _ in range(1):
        hourly_posts = get_posts(subreddit)
        upvotes = 0
        comments = 0
        for v in hourly_posts.values():
            upvotes += v[0]
            comments += v[1]
        t = datetime.datetime.now()
        timeindex.append(t.strftime("%c"))
        data.append(
            [
                get_subscribers(subreddit),
                get_active(subreddit),
                len(hourly_posts),
                upvotes,
                comments,
            ]
        )
        if postdata == {}:
            postdata = hourly_posts
        else:
            postdata = postdata.update(hourly_posts)
    array1 = np.array(data)
    dti = pd.DatetimeIndex(timeindex)
    df = pd.DataFrame(
        array1,
        index=dti,
        columns=[
            "Subs",
            "Active users",
            "Posts/hour",
            "Post upvotes/hour",
            "Comments/hour",
        ],
    )
    df2 = pd.DataFrame.from_dict(
        postdata, orient="index", columns=["Scores", "Number of Comments"]
    )
    return df, df2


if __name__ == "__main__":
    subreddit = "learnpython"
    subreddit_data = main(subreddit)
    for i, df in enumerate(subreddit_data):
        filename = subreddit + "data" + str(i) + ".csv"
        existing_file = Path(path / filename)
        if existing_file.is_file():
            print(f"Adding to {filename}...")
            df.to_csv(path / filename, mode="a", header=False)
        else:
            df.to_csv(path_or_buf=path / filename)
            print(f"Creating {filename}...")

    plot_activity("learnpython", on=False)
    plot_users_vs_act("learnpython", on=False)
    plot_users_vs_tod("learnpython", on=False)

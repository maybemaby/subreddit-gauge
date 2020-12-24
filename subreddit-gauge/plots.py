#! python3
# plotting functions for various comparisons

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

path = r"C:/Users/BrandonMa/Python projects/subreddit-gauge/"
subreddit = "learnpython"


def plot_activity(subreddit, on=True):
    """Plots chosen subreddit's subs, active users,
    posts/hour, and upvotes/hour against time.

    Input
    ------
    string: subreddit name
    on: Default = True, False to turn off plot.
    Return
    -----
    plot
    """
    if on == True:
        df = pd.read_csv(path + subreddit + "data0.csv", index_col=0)
        df.plot(subplots=True, figsize=(8, 8), xlabel="Time")
    elif on == False:
        return


def plot_users_vs_activity(subreddit, on=True):
    """Plots chosen subreddit's posts/hour and comments/hour
    against amount of users active in that hour.

    Input
    -----
    string: subreddit name
    on: Default = True, False to turn off plot.
    Return
    ------
    plot
    """
    if on == True:
        # Only use the desired data for our dataframe and don't use the time index
        df = pd.read_csv(
            path + subreddit + "data0.csv",
            usecols=["Active users", "Posts/hour", "Comments/hour"],
            index_col=False,
        )

    elif on == False:
        return


def plot_users_vs_tod(subreddit, on=True):
    """Plots chosen subreddit's average active users throughout the day.

    Input
    ------
    string: subreddit name
    on: default = True, False to turn off plot.
    Return
    -----
    plot
    """
    if on == True:
        df = pd.read_csv(path + subreddit + "data0.csv", usecols=[0, 2])
        df.columns = ["datetime", "Active users"]
        df["datetime"] = pd.to_datetime(df["datetime"])
        fig, axs = plt.subplots(figsize=(12, 4))
        df.groupby(df["datetime"].dt.hour)["Active users"].mean().plot(
            kind="bar", rot=0, ax=axs
        )
        plt.xlabel("Time of day:Hour")
        plt.ylabel("Active Users")
    elif on == False:
        return

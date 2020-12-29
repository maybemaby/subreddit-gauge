#! python3
# plotting functions for various comparisons

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

path = Path.home() / "Python projects/subreddit-gauge/"
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
    4 line plots
    """
    if on == True:
        df = pd.read_csv(path + subreddit + "data0.csv", index_col=0)
        df.plot(subplots=True, figsize=(8, 8), xlabel="Time")
        plt.show()
    elif on == False:
        return


def uva_df(subreddit, on=True):
    """Creates dataframe of active users, avg Posts/hr,
    and avg comments/hr from csv.

    Input
    -----
    string: subreddit name
    on: Default = True, False to turn off plot.
    Return
    ------
    dataframe
    """
    if on == True:
        # Only use the desired data for our dataframe and don't use the time index
        df = pd.read_csv(
            path + subreddit + "data0.csv",
            usecols=["Active users", "Posts/hour", "Comments/hour"],
            index_col=False,
        )
        df.sort_values("Active users", inplace=True)
        bin = []
        for x in range(700, 1601, 100):
            filt = (df["Active users"] >= x) & (df["Active users"] < x + 100)
            if filt.any():
                df2 = df[filt]
                df2.loc[:, ["Active users"]] = f"{x}-{x+100}"
                df2.loc["averages"] = [
                    f"{x}-{x+100}",
                    df2["Posts/hour"].mean(),
                    df2["Comments/hour"].mean(),
                ]
                df3 = df2.loc["averages"]
                bin.append(df3)
        df4 = pd.concat(bin)
        user_series = df4.loc["Active users"]
        user_series.reset_index(drop=True, inplace=True)
        posts_series = df4.loc["Posts/hour"]
        posts_series.reset_index(drop=True, inplace=True)
        comment_series = df4.loc["Comments/hour"]
        comment_series.reset_index(drop=True, inplace=True)
        frame = {
            "Active users": user_series,
            "Avg. Posts/hr": posts_series,
            "Avg. Comments/hr": comment_series,
        }
        resultdf = pd.DataFrame.from_dict(frame)
        return resultdf.set_index("Active users")
    elif on == False:
        return


def plot_users_vs_act(subreddit, on=True):
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
        plot2_df = uva_df(subreddit, on=True)
        plot2_df.plot.bar(stacked=True)
        plt.show()
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
    bar chart plot
    """
    if on == True:
        df = pd.read_csv(path + subreddit + "data0.csv", usecols=[0, 2])
        df.columns = ["datetime", "Active users"]
        df["datetime"] = pd.to_datetime(df["datetime"])
        fig, axs = plt.subplots(figsize=(12, 8))
        df.groupby(df["datetime"].dt.hour)["Active users"].mean().plot(
            kind="bar", rot=0, ax=axs
        )
        plt.xlabel("Time of day:Hour")
        plt.ylabel("Average Active Users")
        axs.set_yticks(np.arange(0, 1601, 100))
        plt.show()
    elif on == False:
        return
import csv
import os
import warnings
from pprint import pprint

import tweepy
from tweepy import api

warnings.filterwarnings('ignore')

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
response = client.search_recent_tweets("Student loan forgiveness",
                                       tweet_fields="author_id,created_at,id,in_reply_to_user_id,public_metrics,text",
                                       user_auth=True)
tweets = response.data

tweet_fields = ["experiment_id", "text", "tweet_id",
                "likes", "quotes", "replies", "retweets", "author_id"]

experiment_id = 0
with open("data/tweets.csv", "w+") as tweets_file:
    tweets_csv = csv.writer(tweets_file)
    tweets_csv.writerow(tweet_fields)

    for tweet in tweets:
        text = tweet.text
        tweet_id = tweet.id
        likes = tweet.public_metrics.get("like_count")
        quotes = tweet.public_metrics.get("quote_count")
        replies = tweet.public_metrics.get("reply_count")
        retweets = tweet.public_metrics.get("retweet_count")
        author_id = tweet.author_id

        tweets_csv.writerow([experiment_id, text, tweet_id, likes, quotes, replies, retweets, author_id])
        experiment_id += 1

        # author = client.get_user(id=author_id, tweet_fields="created_at,public_metrics", user_auth=True)

        # author_created_at = author.data.created_at
        # author_location = author.data.location
        # author_username = author.data.username
        # author_verified = author.data.verified

        # print(author.data.public_metrics)

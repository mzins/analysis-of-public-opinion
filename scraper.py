"""
This script pulls data from 
"""
import tweepy
import os
import csv
from pprint import pprint

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# authentication 
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) 

tweet_fields = ["experiment_id", "experiment_group", "text", "tweet_id", "likes", "retweets", "created_at", "user_id"]
tweets_file = open("data/tweets.csv", "w")
tweets_csv = csv.writer(tweets_file)
tweets_csv.writerow(tweet_fields)

user_fields = ["user_id", "created_at", "description", "location", "followers_count", "screen_name", 
                "statuses_count", "favourites_count", "verified"]
users_file = open("data/users.csv", "w")
users_csv = csv.writer(users_file)
users_csv.writerow(user_fields)

experiment_id = 0

for exp_group in ["usedgov", "foxnews", "cnn"]:
    tweepy_cursor = tweepy.Cursor(api.search_tweets, q=f"student loan @{exp_group} -is:retweet", count=100).items(100)

    for t in tweepy_cursor:
        tweet = t._json

        text = tweet.get("text")
        tweet_id = tweet.get("id_str")
        likes = tweet.get("favorite_count")
        retweets = tweet.get("retweet_count")
        created_at = tweet.get("created_at")
        user = tweet.get("user")
        user_id = user.get("id")

        tweets_csv.writerow([experiment_id, exp_group, text, tweet_id, likes, retweets, created_at, user_id])

        user_created_at = user.get("created_at")
        user_description = user.get("description")
        user_location = user.get("location")
        user_followers = user.get("followers_count")
        user_screen_name = user.get("screen_name")
        user_statuses_count = user.get("statuses_count")
        user_favourites_count = user.get("favourites_count")
        user_verified = user.get("verified")

        users_csv.writerow([user_id, user_created_at, user_description, user_location, user_followers, user_screen_name, 
                            user_statuses_count, user_favourites_count, user_verified])
        
        experiment_id += 1

tweets_file.close()
users_file.close()
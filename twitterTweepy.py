import tweepy  # https://github.com/tweepy/tweepy
import csv
import pandas as pd

consumer_key = " "
consumer_secret = " "
access_key = ""
access_secret = ""

count = 0

def get_all_tweets(screen_name):
    global count

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=1000)
    alltweets.extend(new_tweets)
    outtweets = [[tweet.id, tweet.text] for tweet in alltweets]

    with open(f'C:/Users/Semih/PycharmProjects/firstProjectEver/eclat/Apriori-Eclat-master/mixed/long/{count}_{screen_name}_long-tweets.csv', 'w',encoding="utf-8",errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow(["name","text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':

    df = pd.read_csv("users.csv",sep=",", encoding="ISO-8859-1")
    for x in range(len(df)):
        count+=1
        name = str(df.values[x][0])
        get_all_tweets(name)

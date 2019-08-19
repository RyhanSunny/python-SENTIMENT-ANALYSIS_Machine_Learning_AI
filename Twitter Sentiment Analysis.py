import tweepy
import tweepy as tweepy
from textblob import TextBlob

# wiki = TextBlob('Sunny is angry he never get avocados for Christmas')
# wiki.tags
# wiki.words
# wiki.sentiment.polarity


# Using Twitter API created a twitter app and generated access tokens
from tweepy.auth import AuthHandler

consumer_key = "xymCHFLBMXmvStjskVbQV9ubP"
consumer_secret = "5ULTY4FyECVc7w4xMXRlH2KUej9erJw9e2rYxmzklRJ0rRb6Ci"

access_token = "2328844606-L8LSWoVRuKa4LATCVcL6YgeWso1rr2gB6duDmZx"
access_token_sectet = "b061CB0XDN3vEl7psSJAmrSZuMWLifwDbi8JLODWWnlNq "

# logging in (O auth not zero)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectet)

api = tweepy.API(auth)

# now that we have our API set up we can perform a whole bunch of possible methods
# such as: create tweet, delete tweet, find twitter user

# for our use case we will collect tweets using a certain keyword

# search keyword:
public_tweets = api.search('Trump')
# print all out in the terminal
for tweet in public_tweets:
    print(tweet.text)
    # time to analyze each tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    # POLARITY measures how positive or negative a tweet is
    # SUBJECTIVITY measures how much of an OPINION it is VS how much of it is FACTUAL


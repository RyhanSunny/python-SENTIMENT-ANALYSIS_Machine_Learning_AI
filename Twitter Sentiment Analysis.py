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


import tweepy
import tweepy as tweepy
from textblob import TextBlob

# textblob test
# wiki = TextBlob('Sunny is angry he never get avocados for Christmas')
# wiki.tags
# wiki.words
# wiki.sentiment.polarity


# Using Twitter API created a twitter app and generated access tokens
from tweepy.auth import AuthHandler

consumer_key = "xymCHFLBMXmVstjskVbQV9ubP"
consumer_secret = "5ULTY4FyECVc7w4xMXRlH2kYej9erJw9e2rYxmzklRJ0rRb6Ci"

access_token = "2328844606-ZWTEMGMOpWA5dBo7r0QgUcbGopNnPcE13LG82vu"
access_token_secret = "Q42Nq8CdXVPHAiCEnH3UWCHfY3Rx8rnuxFo1LG4ritn7o"

# logging in (O auth not zero)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

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
    print("")
    # POLARITY measures how positive or negative a tweet is
    # SUBJECTIVITY measures how much of an OPINION it is VS how much of it is FACTUAL
# NOTE THIS IS A PROTOTYPE SCRIPT, MUCH MORE TO IMPROVE ON LATER
# FOR LEARNING PURPOSES

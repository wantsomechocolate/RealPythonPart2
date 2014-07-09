#twitter.py

import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='#python')
for t in tweets:
    print t.created_at,  t.text, '\n'



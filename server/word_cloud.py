#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
consumer_key = "eCOrAJmP6PsNo1B86xwjA0aOJ"
consumer_secret = "kjL8ssd6Y9RQsMcEOoZMj9od35ZDZZ08z3cbEzSK6vHjEtRHSC"
access_key = "737867543415820288-BjJj3WNOJXX94pcXqnYbANX8J6ObNp9"
access_secret = "zUe2oQSu5oEWyKidiQdS5d5HmaAnXptGnViShkH4EZE6a"

class Worldcloud():
    @staticmethod
    def get_tweets(screen_name):
        alltweets = []  
        if screen_name is None or len(screen_name) == 0:
            return alltweets
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode="extended")

        alltweets.extend([[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in new_tweets] )
        
        #save the id of the oldest tweet less one
        # print(alltweets[-1])
        oldest = int(alltweets[-1][0]) - 1   
        
        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            # print(f"getting tweets before {oldest}")
            
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode="extended")
            alltweets.extend([[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in new_tweets] )
            
            # print(alltweets[-1])
            oldest = int(alltweets[-1][0]) - 1   
            # print(f"...{len(alltweets)} tweets downloaded so far")
        return alltweets


if __name__ == '__main__':
	#pass in the username of the account you want to download
	Worldcloud.get_tweets("soicfinance")
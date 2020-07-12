import tweepy as tp
from time import sleep
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

# Set up OAuth and integrate with API
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


message = "@Harry_Styles you don't know how happy you make me everyday. I wish I can meet you one day and hug you, follow me please? i love you! — "

def tweet():
    num = 404
    while num <= 18021:
        try:   
            api.update_with_media('creep.png',message + str(num))
            print("Tweet sent " + str(num))
            num += 1
        except tp.error.TweepError:
            print("Waiting...")
            sleep(15*60)
 
tweet()

#error code
#tweepy.error.TweepError: [{'code': 226, 'message': "This request looks like it might be automated.
#To protect our users from spam and other malicious activity, we can't complete this action right now. Please try again later."}]

#This is twitter mmodule
#This is third file to execute.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Sentiment_module as s

#consumer key, consumer secret, access token, access secret.
ckey="I have removed my consumer key"
csecret="I have removed my consumer secret"
atoken="I have removed my aceess token"
asecret="I have removed my access secret"



class listener(StreamListener):

    def on_data(self, data):
        try:

            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])

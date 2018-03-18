'''
Created on Aug 2, 2017

@author: hdusr
'''
#!/usr/bin/env python2


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1528192604-pWoRvXqulgbS1LBwT66qYvsy8L5zdOomapCHO4g"
access_token_secret = "vlmN10qPajHwJViSuPmcDZUHVtwjalm7QPmtzJnZN8zAG"
consumer_key = "OB48XMh4S1DEVJ4tTsphVg9px"
consumer_secret = "qwivWEKmG22jAeXn7VxUr6ETxQOwuRG4KKZLk00DQFeYbWCfhv"


#This is a basic listener that  prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['India', 'China', 'America'])
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from http.client import IncompleteRead

#My credentials
access_token = "4895748430-ZGdr10BYg963Mfqd9WdS04hTUMdRDw2pqPnYxPS"
access_token_secret = "kf8bQg1FP5J3ao2C88znHiWsFQyctEwpwJBMdvV8Qzmrc"
consumer_key = "LrGoAHYrkEZ2lDfyNE08STTQd"
consumer_secret = "1n4rjS1MnAQOZWGb8OpnKS672FuMbHDJqD4qiBGy9lnonPJRc9"

# Parushs' credentials
# access_token = "412554094-EkOR0nEYSzcdVAgbfq5qF76K8Ght2Sg5VuiPlKC5"
# access_token_secret = "7fw6SqhdwClRBZ6leOwRJv41EofXfnPyKQ8J49Ok0FzCC"
# consumer_key = "tY3kjlugGYfT5tFUSYnwed0wl"
# consumer_secret =  "n3TleJB5f6oqwg2OATeNw6Y60u5auOAwB5UmzqZ6JHzUURw2mp"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        file.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    file = open('vape_tweets.json','a')
    #file = open('sample_tweets.json','a')

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:
        stream = Stream(auth, l)

        stream.filter(track=['ecigs','ecigarettes','vape','vaping','e pen','#vape','#vaper',"#vapecommunity",'vapefam','vape juice','vape ban','vape porn','#antivaping','#fighttheflavor','vape death', 'vaping illness', 'e vaping', 'thc vaping', 'quitlying', 'in2020imgoingtoquit', 'vapingsa', 'truthaboutvaping', 'vapingindustry', 'noecigs4kids', 'iambigvape'])
        #stream.sample()

    except IncompleteRead:
        pass



'''

Alabama
California (3)
Connecticut
Delaware
District of Columbia
Florida, Georgia (3)
Illinois (3)
Indiana (3)
Kansas (2)
Massachusetts (2)
Michigan
Minnesota (3)
Mississippi
Missouri
Montana
Nebraska
New Jersey
New York
Oregon (2)
ennsylvania
Tennessee (2)
Texas
Utah
Virginia.


'''
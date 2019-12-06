import json
import pandas as pd
import matplotlib.pyplot as plt

file1 = open('../all_age_locations.txt','w')



locationCount = 0;
textCount = 0;
placesCount = 0;

tweets_data_path = "../all_age_tweets.json"

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

for tweet in tweets_data:
    
    try:
        tweetGeo = tweet.get('place').get("full_name")
    except:
        tweetGeo = None

    try:
        tweetUserLoc = tweet.get('user').get('location')
    except:
        tweetUserLoc = None

    if(tweetGeo != None):
        key = tweetGeo.encode('ascii', 'ignore').decode('ascii')
        file1.write(key)
        file1.write("\n")
        #print(tweetGeo)
    else:
        if(tweetUserLoc != None):
            key2 = tweetUserLoc.encode('ascii', 'ignore').decode('ascii')
            file1.write(key2)
            file1.write("\n")


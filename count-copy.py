import json

tweets_data_path = "../demo_clean.txt"
file = open('../all_age_tweets.json','a')

tweets_file1 = open(tweets_data_path, "r")
tweets_file2 = open("../vape_tweets.json", "r")

tweets_data = []

for line in tweets_file2:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print("file loaded")

count = 0

for line in tweets_file1:

	count += 1

	print(count)

	line_split = line.split(",")
	
	age = line_split[2]

	if(True):

		tweet_id = line_split[0]

		for tweet in tweets_data:

			tweet_identity = tweet.get('id_str')

			if(float(tweet_id) == float(tweet_identity)):
				file.write(json.dumps(tweet))
				file.write("\n")
				break
		








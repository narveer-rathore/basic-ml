import tweepy

from textblob import TextBlob

TOPIC_TO_SEARCH = "ISIS"
OUTPUT_CSV_FILE = "tweets_label.csv"

# twitter api constants
access_token = ""
access_token_secret = ""
user_key = ""user_
secret = ""


auth = tweepy.OAuthHandler(user_key, user_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = api.search(TOPIC_TO_SEARCH)


file = open(OUTPUT_CSV_FILE, 'w')

for tweet in tweets:
	analyzed = TextBlob(tweet.text)
	res = ''
	if analyzed.sentiment.polarity > 0.0:
		res = "positive"
	elif analyzed.sentiment.polarity < 0.0:
		res = "negative"
	else:
		res = "neutral"
	file.write(','.join(map(str, [analyzed.sentiment.polarity, analyzed.sentiment.subjectivity, res, tweet.text, '\n'])))

file.close()

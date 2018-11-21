import praw
import time
import json
import os.path
import twitter
from datetime import datetime

def readConfig():

	if (os.path.isfile('config.json')):

		with open('config.json', 'r') as f:
			data = json.load(f)
			f.close()

			return data
	else:

		config = {
		"Reddit": [ 

		{"client_id": "X", "client_secret": "X", "username": "X", "password": "X" }
		], 
		"Twitter": [ 

		{"access_key": "X", "access_secret": "X", "consumer_key": "X", "consumer_secret": "X"}
		]
		}
		with open('config.json', 'w') as secret_info:
			json.dump(config, secret_info, indent=4, sort_keys=True)

		return
	

def main():
	config = readConfig()

	print("Loaded Json Config Data")

	redditInfo = config['Reddit'][0]

	reddit = praw.Reddit(user_agent=redditInfo['username'],
			client_id=redditInfo["client_id"],
			client_secret=redditInfo["client_secret"],
			username=redditInfo["username"],
			password=redditInfo["password"])

	twitterInfo = config['Twitter'][0]
	twitterApi = twitter.Api(consumer_key=twitterInfo['consumer_key'],
		consumer_secret=twitterInfo['consumer_secret'],
		access_token_key=twitterInfo['access_key'],
		access_token_secret=twitterInfo['access_secret'])


	subreddit = reddit.subreddit('DetroitRedWings')
	print()
	print(reddit.user.me())
	print()
	time.sleep(1)

	for submission in subreddit.hot(limit=2):
		if (submission.author == "OctoMod"):
	 		#submission.reply("Test")
	 		print("Found submission titled: " + submission.title)

	updates = twitterApi.GetUserTimeline(screen_name='DRWProspects', count=10)

	message = ("TEST\n")
	for x in updates:
		d = datetime.strptime(x.created_at,'%a %b %d %H:%M:%S %z %Y');
		if (d.date() == datetime.today().date()):
			message = message + (x.text + "\n\n").replace("#RedWings", " ")

	message = message + "I am a bot and this action was performed automatically. More information can be found at [My GitHub](https://github.com/randykinne/DRW-Prospect-Reddit-Bot)"
	message = message + "\nData Source: https://twitter.com/DRWProspects"
	print(message)
	submission.reply(message)
	print("Message posted on Reddit.")
	

main()
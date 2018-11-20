import praw
import time
import json
import os.path

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

	bot = praw.Reddit(user_agent=redditInfo['username'],
			client_id=redditInfo["client_id"],
			client_secret=redditInfo["client_secret"],
			username=redditInfo["username"],
			password=redditInfo["password"])

	subreddit = bot.subreddit('DetroitRedWings')
	print()
	print(bot.user.me())
	print()
	time.sleep(1)

	for submission in subreddit.hot(limit=2):
		if (submission.author == "OctoMod"):
	 		#submission.reply("Test")
	 		print("Found submission titled: " + submission.title)

main()


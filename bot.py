## 
## DRWProspectBot v1 (12/5/2018)
## A twitter-subreddit bot for the r/DetroitRedWings subreddit
## 
## by Randy Kinne
##
## TODO: format config default better
## TODO: add verbose setting in config, then read to determine verbosity
## TODO: add confirmation setting in config, then read to determine whether a confirmation for bot actions is necessary
## TODO: Reformat the printed messages to user

import praw
import time
import json
import os.path
import twitter
from datetime import datetime

##
## @brief      Reads a configuration.
##
## @return     { Returns the config file }
##
def readConfig():

	# if 'config.json' file exists in same path as this file, open it
	if (os.path.isfile('config.json')):

		# open config file, return the data loaded as json
		with open('config.json', 'r') as f:
			data = json.load(f)
			f.close()

			return data

	# if 'config.json' file does not exist
	else:

		# create basic outline for file 
		# need to format this better, it's a mess
		config = {
		"Reddit": [ 

		{"client_id": "X", "client_secret": "X", "username": "X", "password": "X" }
		], 
		"Twitter": [ 

		{"access_key": "X", "access_secret": "X", "consumer_key": "X", "consumer_secret": "X"}
		]
		}

		# create the file, indent=4 and sort_keys=True to add readability to the json file
		with open('config.json', 'w') as secret_info:
			json.dump(config, secret_info, indent=4, sort_keys=True)

		# return the default config which will attempt to log in, it won't work and it'll let the user know 
		return config
	
##
## @brief      Main function
## 
## @return 	   N/A
##
def main():

	# Attempt to get the config, see function readConfig() above
	config = readConfig()

	# verbose messages for user
	print("Loaded Json Config Data")

	# declare redditInfo to make it easier to get info from the config
	redditInfo = config['Reddit'][0]

	# set praw reddit user info with the info from the config
	reddit = praw.Reddit(user_agent=redditInfo['username'],
			client_id=redditInfo["client_id"],
			client_secret=redditInfo["client_secret"],
			username=redditInfo["username"],
			password=redditInfo["password"])

	# declare twitterInfo to make it easier to get info from the config
	twitterInfo = config['Twitter'][0]

	# set python-twitter user info with the info from the config
	twitterApi = twitter.Api(consumer_key=twitterInfo['consumer_key'],
		consumer_secret=twitterInfo['consumer_secret'],
		access_token_key=twitterInfo['access_key'],
		access_token_secret=twitterInfo['access_secret'],
		tweet_mode='extended')

	# set the subreddit name for praw
	subreddit = reddit.subreddit('DetroitRedWings')

	#printing the name of the reddit user - outdated
	print()
	print(reddit.user.me())
	print()

	# wait a sec, no reason
	time.sleep(1)

	# finds the daily reddit post by OctoMod (bot). It's always the 2nd post sorted by hot
	for submission in subreddit.hot(limit=2):
		if (submission.author == "OctoMod"):
			# print name of the submission to ensure the name is correct
	 		print("Found submission titled: " + submission.title)

	# get the user timeline from twitter user 'DRWProspects', they wouldn't post more than 15 in a single day 
	updates = twitterApi.GetUserTimeline(screen_name='DRWProspects', count=15)

	# preface message with yesterday's results so users know which day the scores happened on, then newline for formatting
	message = ("Yesterday's Results:\n")

	# get every update from the twitter user
	for x in updates:
		# format the date into a format python can recognize
		d = datetime.strptime(x.created_at,'%a %b %d %H:%M:%S %z %Y');
		# check if the date was the same as today, necessary to ensure that you aren't getting tweets from the past
		if (d.date() == datetime.today().date()):
			# append the tweet to the message while replacing #RedWings with a space
			# the twitter user adds #RedWings to the end of every tweet, could get redundant or annoying
			# newlines for formatting
			message = message + (str(x.full_text) + "\n\n").replace("#RedWings", " ")

	# after all tweets have been added to message, add this to bottom of message posted to reddit so users have more information about this project as well as the data source
	message = message + "I am a bot and this action was performed automatically. More information can be found at [My GitHub](https://github.com/randykinne/DRW-Prospect-Reddit-Bot)"
	message = message + "\n\nData Source: https://twitter.com/DRWProspects"

	# print the message to the screen so the user sees what will be posted on Reddit
	print(message)

	# finally post the message on Reddit
	submission.reply(message)

	# confirmation dialog
	print("Message posted on Reddit.")
	
# this is necessary, I once forgot this and nothing happened when I ran the program, spent several hours figuring out why
# pretty self explanatory though
main()

##
## eop
##

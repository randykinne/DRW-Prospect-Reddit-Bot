import praw
import time

bot = praw.Reddit(user_agent='Username',
		client_id='Id',
		client_secret='Secret',
		username='Username',
		password='Password')

subreddit = bot.subreddit('DetroitRedWings')
print()
print(bot.user.me())
print()
time.sleep(1)

for submission in subreddit.hot(limit=2):
	if (submission.author == "OctoMod"):
 		#submission.reply("Test")
 		print("Found submission titled " + submission.title)




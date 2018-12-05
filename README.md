# DRW Prospect Reddit Bot
This is a twitter subreddit bot written in [Python](https://www.python.org/). It currently adds all daily posts from _DRWProspects_ twitter account into a single post to the Detroit Red Wings subreddit's daily discussion or game day thread post.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for different purposes. See *Use* section for notes on how to use the bot.

### Prerequisites
You will need to have [Python 3.6+](https://www.python.org/downloads/), [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html), and [python-twitter](https://python-twitter.readthedocs.io/en/latest/installation.html)

***If you've just installed Python3, pip3 will be included but might not be up-to-date. Update it by running the command:

```
python3 -m pip install --upgrade pip
```

pip3 will now be updated to version 18.1
For more information or more help on using pip3, reference [Using pip3 to install Python modules](https://help.dreamhost.com/hc/en-us/articles/115000699011-Using-pip3-to-install-Python3-modules)

Now install the necessary modules with the following commands:

```
pip3 install praw
```
```
pip3 install python-twitter
```

### Installing
Clone or download the respository.

## Use
In Terminal or Command Prompt, run the following command in the directory of the repo:

```
python3 bot.py
```

If the config.json file doesn't exist yet, it will be generated. 

Replace each 'x' with the correct values to log into Reddit and Twitter, then run the previous command again. If everything was installed correctly, the program should state the correctly found Reddit thread, as well as list all of the tweets found, and then post the tweets found to the reddit thread.

This command/program will need to be ran again each time it is used.

## Adjustment/Repurpose
The program is currently configured for the specific purpose of posting information about Detroit Red Wings prospects onto the [r/DetroitRedWings](reddit.com/r/DetroitRedWings) subreddit daily post. 

***There are future plans to change adjustment options to config.json rather than hardcode, but this is currently not the case.***

To use for another purpose, open bot.py in your favorite editor and edit the following:

Change the name of the subreddit:
```
subreddit = reddit.subreddit('DetroitRedWings')
```

Change the way the Reddit thread is found, unless you are looking for posts from a specific user within the top 2 Hot, in which case then you only need to change the name of the user:
```
for submission in subreddit.hot(limit=2):
		if (submission.author == "OctoMod"):
	 		print("Found submission titled: " + submission.title)
```

Change the Twitter user and the amount of tweets:
```
updates = twitterApi.GetUserTimeline(screen_name='DRWProspects', count=10)
```

Adjust the text added around the data pulled from the twitter updates:
```
message = ("Yesterday's Results:\n")
	for x in updates:
		d = datetime.strptime(x.created_at,'%a %b %d %H:%M:%S %z %Y');
		if (d.date() == datetime.today().date()):
			message = message + (str(x.full_text) + "\n\n").replace("#RedWings", " ")

	message = message + "I am a bot and this action was performed automatically. More information can be found at [My GitHub](https://github.com/randykinne/DRW-Prospect-Reddit-Bot)"
	message = message + "\n\nData Source: https://twitter.com/DRWProspects"
```

## Contributing
Feel free to contribute. When submitting pull requests, include details on changes made.

## Future Plans
- Changing data source information from hardcode to config.json to make program more usable for a variety of purposes
- Adding prompts for user confirmation for various events in the program to allow user to ensure that the bot is operating correctly

## Examples
Check out [u/DRWProspectBot on Reddit](https://www.reddit.com/u/drwprospectbot).

## Authors
* **Randy Kinne** - *All Work* - [randykinne](https://github.com/randykinne)

## License
Licensed under the [GNU General Public License v3.0](LICENSE).

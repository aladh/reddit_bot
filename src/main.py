import yaml
import os
import praw
import random
from datetime import datetime
# noinspection PyUnresolvedReferences
from reply_chooser import ReplyChooser

with open(f'{os.path.dirname(__file__)}/quotes.yml') as f:
    yaml_string = f.read()

string_quotes = yaml.load(yaml_string)

quotes = string_quotes

reddit = praw.Reddit('tyrion')

subreddit = 'freebots'
trigger = 'tyrion'

reply_chooser = ReplyChooser(random, quotes)

print('Listening for triggers...')

for comment in reddit.subreddit(subreddit).stream.comments(skip_existing=True):
    try:
        if trigger in comment.body.lower():
            reply = reply_chooser.reply(comment)

            print(f'{datetime.utcnow()} - u/{comment.author.name} says: "{comment.body}". Replying with: "{reply}"')

            comment.reply(reply)
    except Exception as e:
        print(f'{datetime.utcnow()} - Exception: ', e)
        continue

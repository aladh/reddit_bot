import os
import praw
import random
from datetime import datetime
from reply_chooser import ReplyChooser
from lambda_quotes import LambdaQuotes
from word_filter import WordFilter
from trigger_recognizer import TriggerRecognizer

with open(f'{os.path.dirname(__file__)}/quotes.txt') as f:
    quotes_file = f.read()

string_quotes = quotes_file.split(sep='\n')

quotes = string_quotes + LambdaQuotes.all()

reddit = praw.Reddit('tyrion')

subreddit = 'freebots'
triggers = ['imp', 'dwarf', 'halfman', 'half-man', 'half man', 'monster', 'demon', 'monkey']

reply_chooser = ReplyChooser(random, quotes)
word_filter = WordFilter(triggers)
trigger_recognizer = TriggerRecognizer(triggers)

print('Listening for triggers...')

for comment in reddit.subreddit(subreddit).stream.comments(skip_existing=True):
    try:
        trigger = trigger_recognizer.has_trigger(comment.body)

        if not trigger:
            continue

        print(f'{datetime.utcnow()} - Triggered by: "{trigger}"')
        print(f'{datetime.utcnow()} - u/{comment.author.name} says: "{comment.body}"')

        reply = reply_chooser.reply(comment)

        if word_filter.is_blocked(reply):
            print(f'{datetime.utcnow()} - WordFilter blocked reply: {reply}')
            continue

        print(f'{datetime.utcnow()} - Replying with: "{reply}"')
        print()

        comment.reply(reply)
    except Exception as e:
        print(f'{datetime.utcnow()} - Exception: ', e)
        continue

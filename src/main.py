import os
import praw
import random
from datetime import datetime
# noinspection PyUnresolvedReferences
from quotes.lambda_quotes import LambdaQuotes
# noinspection PyUnresolvedReferences
from util.reply_chooser import ReplyChooser
# noinspection PyUnresolvedReferences
from util.word_matcher import WordMatcher

with open(f'{os.path.dirname(__file__)}/quotes/quotes.txt') as f:
    quotes_file = f.read()

string_quotes = quotes_file.split(sep='\n')

quotes = string_quotes + LambdaQuotes.all()

reddit = praw.Reddit('tyrion')

subreddit = 'freebots'
triggers = ['imp', 'dwarf', 'halfman', 'half-man', 'half man', 'tyrion bot', 'tyrion-bot']

reply_chooser = ReplyChooser(random, quotes)
word_matcher = WordMatcher(triggers)

print('Listening for triggers...')

for comment in reddit.subreddit(subreddit).stream.comments(skip_existing=True):
    try:
        trigger = word_matcher.is_present(comment.body)

        if not trigger:
            continue

        if comment.author == reddit.user.me():
            continue

        print(f'{datetime.utcnow()} - Triggered by: "{trigger}"')
        print(f'{datetime.utcnow()} - u/{comment.author.name} says: "{comment.body}"')

        reply = reply_chooser.reply(comment)

        print(f'{datetime.utcnow()} - Replying with: "{reply}"')
        print()

        comment.reply(reply)
    except Exception as e:
        print(f'{datetime.utcnow()} - Exception: ', e)
        continue

import random
import praw
import logging
# noinspection PyUnresolvedReferences
from util.word_matcher import WordMatcher
# noinspection PyUnresolvedReferences
from util.reply_chooser import ReplyChooser


class ReplierConfig:
    def __init__(self, triggers, replies, test):
        self.triggers = triggers  # TODO: Allow regex
        self.replies = replies
        self.test = test


class ListenerConfig:
    def __init__(self, subreddit):
        self.subreddit = subreddit


class Bot:
    _listener = None
    _repliers = []

    def __init__(self, account):
        self.account = account

    def listen(self, subreddit):
        self._listener = ListenerConfig(subreddit)
        return self

    def reply(self, triggers, replies, test=False):
        self._repliers.append(ReplierConfig(triggers, replies, test))
        return self

    def run(self):
        logging.info(f'Listening for triggers in r/{self._listener.subreddit}...\n')
        reddit = praw.Reddit(self.account)

        for comment in reddit.subreddit(self._listener.subreddit).stream.comments(skip_existing=True):
            for replier in self._repliers:
                word_matcher = WordMatcher(replier.triggers)
                reply_chooser = ReplyChooser(random, replier.replies)

                try:
                    trigger = word_matcher.is_present(comment.body)

                    if not trigger:
                        continue

                    if comment.author == reddit.user.me():
                        continue

                    reply = reply_chooser.reply(comment)

                    logging.info(f'{"TEST: " if replier.test else ""}Triggered by: "{trigger}"'
                                 f'\nu/{comment.author.name} says: "{comment.body}"'
                                 f'\nReplying with: "{reply}"'
                                 f'\n')

                    if replier.test:
                        continue

                    comment.reply(reply)
                except Exception as e:
                    logging.info(f'Exception: {e}')
                    continue

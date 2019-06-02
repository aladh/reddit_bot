import random
import praw
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
    _replier = None

    def __init__(self, account):
        self.account = account

    def listen(self, subreddit):
        self._listener = ListenerConfig(subreddit)
        return self

    def reply(self, triggers, replies, test=False):
        self._replier = ReplierConfig(triggers, replies, test)
        return self

    def run(self):
        reddit = praw.Reddit(self.account)

        for comment in reddit.subreddit(self._listener.subreddit).stream.comments(skip_existing=True):
            word_matcher = WordMatcher(self._replier.triggers)
            reply_chooser = ReplyChooser(random, self._replier.replies)

            trigger = word_matcher.is_present(comment.body)

            if not trigger:
                continue

            if comment.author == reddit.user.me():
                continue

            reply = reply_chooser.reply(comment)

            if self._replier.test:
                continue

            comment.reply(reply)

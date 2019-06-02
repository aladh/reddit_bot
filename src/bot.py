import random
import praw
# noinspection PyUnresolvedReferences
from util.word_matcher import WordMatcher
# noinspection PyUnresolvedReferences
from util.reply_chooser import ReplyChooser


class ReplierConfig:
    def __init__(self, triggers, replies):
        self.triggers = triggers  # TODO: Allow regex
        self.replies = replies


class ListenerConfig:
    def __init__(self, subreddit):
        self.subreddit = subreddit


class Bot:
    listener = None
    replier = None

    def __init__(self, account):
        self.account = account

    def listen(self, subreddit):
        self.listener = ListenerConfig(subreddit)
        return self

    def reply(self, triggers, replies):
        self.replier = ReplierConfig(triggers, replies)
        return self

    def run(self):
        reddit = praw.Reddit(self.account)
        word_matcher = WordMatcher(self.replier.triggers)
        reply_chooser = ReplyChooser(random, self.replier.replies)

        for comment in reddit.subreddit(self.listener.subreddit).stream.comments(skip_existing=True):
            trigger = word_matcher.is_present(comment.body)

            if not trigger or comment.author == reddit.user.me():
                continue

            reply = reply_chooser.reply(comment)

            comment.reply(reply)

import random


class ReplyGenerator:
    def __init__(self, quotes):
        random.seed()
        self.quotes = quotes

    def random_reply(self, comment):
        quote = random.choice(self.quotes)
        return quote(comment) if callable(quote) else quote

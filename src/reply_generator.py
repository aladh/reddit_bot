class ReplyChooser:
    def __init__(self, random, quotes):
        self.random = random
        self.quotes = quotes
        random.seed()

    def reply(self, comment):
        quote = self.random.choice(self.quotes)
        return quote(comment) if callable(quote) else quote

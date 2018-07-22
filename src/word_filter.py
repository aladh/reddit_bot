class WordFilter:
    def __init__(self, blocked_words):
        self.blocked_words = blocked_words

    def is_blocked(self, text):
        for word in self.blocked_words:
            if word in text:
                return True

        return False

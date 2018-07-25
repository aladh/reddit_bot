import re


class WordMatcher:
    def __init__(self, triggers):
        self.triggers = triggers

    def is_present(self, string):
        # noinspection PyUnusedLocal
        for trigger in self.triggers:
            match = re.search(rf'\b{trigger}\b', string.lower())

            if match:
                return match.group()

import re


class TriggerRecognizer:
    def __init__(self, triggers):
        self.triggers = triggers

    def has_trigger(self, string):
        # noinspection PyUnusedLocal
        for trigger in self.triggers:
            match = re.search(rf'\b{trigger}\b', string.lower())

            if match:
                return match.group()

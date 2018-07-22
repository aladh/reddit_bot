from src.reply_generator import ReplyGenerator

quotes = [
    'hello',
    'hi',
    'bye'
]


class Random:
    def __init__(self, choice_index):
        self.choice_index = choice_index

    # noinspection PyMethodMayBeStatic
    def seed(self):
        return None

    def choice(self, array):
        return array[self.choice_index]


def test_selects_string_quote_using_injected_random():
    reply = ReplyGenerator(Random(0), quotes).random_reply(None)
    assert reply == quotes[0]

from src.reply_generator import ReplyChooser

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


def test_selects_quote_using_injected_random():
    reply1 = ReplyChooser(Random(0), quotes).reply(None)
    reply2 = ReplyChooser(Random(1), quotes).reply(None)
    assert reply1 == quotes[0]
    assert reply2 == quotes[1]
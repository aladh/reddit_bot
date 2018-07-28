from src.util.reply_chooser import ReplyChooser

quotes = [
    'hello',
    'hi',
    'bye',
    lambda comment: f'Hi, {comment.author.name}',
    lambda comment: f'You said {comment.body.split()[0]}'
]


class Random:
    def __init__(self, choice_index):
        self.choice_index = choice_index

    # noinspection PyMethodMayBeStatic
    def seed(self):
        return None

    def choice(self, array):
        return array[self.choice_index]


class Comment:
    def __init__(self):
        self.author = Author()
        self.body = 'This is a comment'


class Author:
    def __init__(self):
        self.name = 'foo'


def test_selects_quote_using_injected_random():
    reply1 = ReplyChooser(Random(0), quotes).reply(None)
    reply2 = ReplyChooser(Random(1), quotes).reply(None)
    assert reply1 == quotes[0]
    assert reply2 == quotes[1]


def test_handles_lambda_quote_with_author():
    reply = ReplyChooser(Random(3), quotes).reply(Comment())
    assert reply == 'Hi, foo'


def test_handles_lambda_quote_with_body():
    reply = ReplyChooser(Random(4), quotes).reply(Comment())
    assert reply == 'You said This'

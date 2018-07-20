from .reply_generator import ReplyGenerator

quotes = [
    'hello'
]


def test():
    assert ReplyGenerator(quotes).random_reply(None) == quotes[0]
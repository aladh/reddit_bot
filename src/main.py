import os
import logging
# noinspection PyUnresolvedReferences
from quotes.lambda_quotes import LambdaQuotes

# noinspection PyUnresolvedReferences
from bot import Bot

logging.basicConfig(filename=f'{os.environ.get("LOG_FILE_DIR")}/reddit_bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

with open(f'{os.path.dirname(__file__)}/quotes/quotes.txt') as f:
    quotes = f.read()

Bot(account='tyrion') \
    .listen(subreddit='freebots') \
    .reply(triggers=['imp', 'dwarf', 'halfman', 'half-man', 'half man', 'tyrion bot', 'tyrion-bot'],
           replies=quotes.split(sep='\n') + LambdaQuotes.all()) \
    .run()

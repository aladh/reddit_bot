import yaml
import os

with open(f'{os.path.dirname(__file__)}/quotes.yml') as f:
    yaml_string = f.read()

string_quotes = yaml.load(yaml_string)
FROM python:3.7.2-alpine3.9

WORKDIR /usr/src/app

COPY . ./

RUN pip install pipenv
RUN pipenv install --system --deploy

ENV SUBREDDIT=$SUBREDDIT

CMD ["python", "./src/main.py"]
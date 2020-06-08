FROM python:3

RUN pip install requests

COPY src/slackbot.py /slackbot.py

ENTRYPOINT ["/slackbot.py"]

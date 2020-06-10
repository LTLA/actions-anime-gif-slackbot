FROM python:3

RUN pip install requests

COPY src/slackbot.py /slackbot.py
COPY src/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Post anime GIFs to Slack, because why not?')
parser.add_argument('webhook', type=str, help='URL to an incoming webhook from the Slack API.')
parser.add_argument('--sentiment', type=str, default='*',
    help='Comma-separated strings of possible sentiments. Defaults to \'*\' in which case all available sentiments are used.')
parser.add_argument('--rating', type=int, default=1,
    help='Maximum safe-for-work rating to consider, from 0 (safest) to 4 (not). Defaults to 1.')

args = parser.parse_args()

##############################################
## Filtering the set of available requests. ##
##############################################

import requests
host="https://ltla.github.io/acceptable-anime-gifs/"

if args.rating < 4: # highest value is 4.
    by_rating=[]
    for rating in range(args.rating+1):
        r = requests.get(host + "rating/" + str(rating))
        by_rating+=r.json()
else:
    by_rating=None

if args.sentiment == '*':
    by_sentiment=None
else:
    sentiments=args.sentiment.split(',')
    by_sentiment=[]
    for sent in sentiments:
        s = requests.get(host + 'sentiment/' + sent)
        by_sentiment+=s.json()

if by_rating is None and by_sentiment is None:
    available = requests.get(host + "entry")
    choices = range(available.json())
elif by_rating is None:
    choices = by_sentiment
elif by_sentiment is None:
    choices = by_rating
else:
    choices = list(set(by_sentiment) & set(by_rating))

###################################
## Picking a GIF and posting it. ##
###################################

import random
chosen = random.choice(choices)

gif_info = requests.get(host + "entry/" + str(chosen))
gif_info = gif_info.json()

template = """{{
  "text":"Dude, where\'s my GIF?",
  "blocks":[
    {{
        "type": "image",
        "title": {{
            "type": "plain_text",
            "text": "{description}"
        }},
        "image_url": "{url}",
        "alt_text": "Ooops! Look like the GIF didn\'t show up. Get your fix at https://myanimelist.net/anime/{show_id}."
    }}
  ]
}}"""

body = template.format(description=gif_info['description'], url=gif_info['url'], show_id=gif_info['show_id'])
requests.post(args.webhook, data=body)

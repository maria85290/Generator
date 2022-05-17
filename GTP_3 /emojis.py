'''
Este modulo é reponsavel pela atribuiçao de emojis ao post
'''
from random import choice
import emoji #https://carpedm20.github.io/emoji/
import pandas as pd
import os
import json
import requests

## Extrair avaliçoes communs no snopes
evaluations = []
for file in os.listdir("../../extractors/Snopes/extractions"):
        with open("../../extractors/Snopes/extractions/" + file) as f:
            data = json.load(f)
            f.close()
        if data['evaluation'] not in evaluations:
            evaluations.append(data['evaluation'])

def sentimentEmoji():
    
    url = "http://kt.ijs.si/data/Emoji_sentiment_ranking/index.html"

    r = requests.get(url)
    df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    df.columns = [c.replace(' ', '_') for c in df.columns]
    df = df[df['Occurrences[5...max]']> 400]
    negative_emojis  = list(df[df['Sentiment_score[-1...+1]'] < 0 ].Char)
    positive_emojis = list(df[df['Sentiment_score[-1...+1]'] > 0].Char)
    return negative_emojis, positive_emojis



def emojis (evaluation, dic_emojis):
    return choice(dic_emojis[evaluation]) 



def emojis_selector (evaluation):
    negative_emojis, positive_emojis = sentimentEmoji()

    dic_emojis = {'false' : negative_emojis ,
                'true' : positive_emojis ,
                'labeled-satire' : negative_emojis,
                'miscaptioned' : negative_emojis,
                'mostly-false' : negative_emojis,
                'misattributed' : negative_emojis,
                'mixture' : negative_emojis,
                'scam' : negative_emojis,
                'mostly-true': positive_emojis,
                'originated-as-satire' : negative_emojis,
                'outdated' : negative_emojis,
                'correct-attribution' : negative_emojis,
                'unproven' : negative_emojis,
                'research-in-progress' : positive_emojis,
                'recall' : negative_emojis,
                'legit' : negative_emojis,
                'legend' : negative_emojis}



    return (emojis (evaluation, dic_emojis))
 

'''
Este modulo é reponsavel pela atribuiçao de emojis ao post.
Baseia-se no lexico http://kt.ijs.si/data/Emoji_sentiment_ranking/index.html
que atribui a cada emojie uma emoção
'''

from random import choice
from numpy import negative, positive
import pandas as pd




def emojis_sellection (evaluation):

    ## Encontrar o sentimento a partir da avaliação da noticia.

    if evaluation in ['true','mostly-true', 'research-in-progress']:
        sentiment = 'positive'
    else:
        sentiment = 'negative'

    data = pd.read_csv('emojis_sentiment_lexicon.csv')
    list_emojis=[]
    for index, row in data.iterrows():
        if row['classification'] == sentiment:
            list_emojis.append(row['emojis'])
    print(list_emojis)
    return list_emojis



def main(evaluation="false"):
  emojis_sellection(evaluation)
  
  
if __name__ == '__main__':
    main()
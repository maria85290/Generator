
## Imports necessarios

import os
import re
import json
import pandas as pd
import random
import nltk
nltk.download('stopwords')
nltk.download('omw-1.4')
from keybert import KeyBERT

def capslock(data):
    
    #text = re.sub(r'[^\w\s]', '', data) 
    text = data
    words_allegation = [word.lower() for word in text.strip('\n').split() ]
    
    
    ## Definir o modelo
    kw_model = KeyBERT()
    words_bert = [word for word, value in kw_model.extract_keywords(docs=text, keyphrase_ngram_range=(1,1))]
                                        
    allegation =  []
    
    for word in text.strip('\n').split():
        if word.lower() in words_bert:
            allegation.append(word.upper())
        else:
            allegation.append(word)
    
    allegation = ' '.join(allegation)
    post = []

    #emoji.emojize(':thumbs_up:')
    post.append(allegation)
    #+ choice(dic[data['evaluation']])
    return ' '.join(post)


def main(text):
  capslock (text)
  
  
if __name__ == '__main__':
    main()
'''
This is the main file of the generator
'''

import json
from pprint import pformat

from matplotlib.font_manager import json_load
import readNews
import sentimentAnalysis

def clean (ListSentences):

    l = [s.replace("\"","\'") for s in ListSentences]

    return l


            

def main(): 
    url = "https://poligrafo.sapo.pt/fact-check/portugal-e-o-pais-da-uniao-europeia-com-mais-emigrantes-espalhados-pelo-mundo"
    newsSentences = readNews.main(url).encode('utf8').decode().split('\n')
    print (newsSentences)
    text =clean(newsSentences)
    lang = 'pt'
    sentiments = sentimentAnalysis.main(text,lang)
    playload = json.loads(sentiments)
    print ({k: v for k, v in sorted(playload.items(), key=lambda item: item[1]['emotions']['surprise'], reverse=True)})

   
 
if __name__ == "__main__": 
	main() 
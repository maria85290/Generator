

# # Hashtags generator


##Imports necessarios

import os
import json
import nltk
nltk.download('wordnet')
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from gensim import corpora
import string
import requests




def clean(sentence):
    
        '''
        Funçao que recebe uma string e retira pontuçao, stop words e lematiza a frase. 
        Retorna uma string;
        '''
    
        stop = set(stopwords.words('english')) #define stop words
        exclude = set(string.punctuation) #define ponctuation for exclude
        lemma = WordNetLemmatizer() 
        
        stop_free = " ".join([i for i in sentence.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split()) ##lematizar
        
        return normalized
    
'''
Ferramenta emotions metter
'''
def emotionsMetter(text,lang):
    print('emotions')
    body = {

        "messages": text,
        "language": lang

        }

    request = requests.post("http://146.59.159.119:9777", json = body)
    return (request.text.encode().decode('unicode-escape') , request.status_code)


'''
Ferramenta emotions metter
'''
from nrclex import NRCLex

def emotionsNRClex(text):
  
    emotion = NRCLex(text)
    emotions_list = emotion.affect_frequencies
    return emotions_list



'''
Funçao que recebe uma string e um idioma e realiza analise de sentimentos (invocando o metodo responsavel);
Retorna as emoçoes associadas num objeto json.
'''


def sentiment_analysis(text, language):  
    
    status_code = 0 ## Valor inicial 
    
    while (status_code != 200):
        emotions, status_code = emotionsMetter(text,language)
        print(emotions)
    playload_emotions = json.loads(emotions)
    #print('emotions')
    
    return playload_emotions
    


'''
Funçao que recebe uma lista de hashtags e verifica se a hashtags tem alguma emoçao;
Retorna as a lista de hahstags onde foi detetada emoçao;
'''

def hashtags_check_emotion(hashtaglist):
        ## call the module of sentiment analysis

        '''
        playload_emotions  = playload = sentiment_analysis(hashtaglist,'en')
   
        sortedByEmotion = {k: v for k, v in sorted(playload_emotions.items(), key=lambda item: (item[1]['emotions']['sadness'] + item[1]['emotions']['surprise'] + item[1]['emotions']['trust'] + item[1]['emotions']['anger'] + item[1]['emotions']['disgust'] + item[1]['emotions']['fear'] + item[1]['emotions']['joy']), reverse=True)}
       # print(sortedByEmotion)

        playload = [] ## add only the hashtags with some percentage of emotion
        
        
        for hashtag, emotion in sortedByEmotion.items():
            if (emotion['emotions']['sadness'] + emotion['emotions']['surprise'] + emotion['emotions']['trust'] + emotion['emotions']['anger'] + emotion['emotions']['disgust'] + emotion['emotions']['fear'] + emotion['emotions']['joy']) > 0:
                #print((emotion['emotions']['sadness'] + emotion['emotions']['surprise'] + emotion['emotions']['trust'] + emotion['emotions']['anger'] + emotion['emotions']['disgust'] + emotion['emotions']['fear'] + emotion['emotions']['joy']) > 0)
                playload.append(hashtag)
                
        '''
       ################ NRC LEX #####################
        playload = [] ## add only the hashtags with some percentage of emotion

        for hashtag in hashtaglist:
            playload_emotions = emotionsNRClex(hashtag)
          #  print(playload_emotions )
            if (playload_emotions['sadness'] + playload_emotions['surprise'] + playload_emotions['trust'] + playload_emotions['anger'] + playload_emotions['disgust'] + playload_emotions['joy'] + playload_emotions['fear']) > 0:
                    playload.append(hashtag)
        #print(playload)


       ################################################
        return (playload)



'''
Função principal que gera hashtags para um dado texto recebido como input
Retorna uma lista de hashtags com emoçao associada e que fazem sentido no contexto do artigo;

utilzia um modelo LDA para realizar a extraçao de topicos.
'''

def generateHashtags (text):
    topicsNun = 6
    passes = 50

    
    
   # text = ' '.join(data['postText']).split('\n')

    text_clean = []
    for sentence in text:
        d = clean(sentence).split()
        text_clean.append(d)

    text_clean = [clean(sentence).split() for sentence in text]   

    dictionary = corpora.Dictionary(text_clean)
    
    matrix = [dictionary.doc2bow(sentence) for sentence in text_clean]
    
    #Define the LDA model
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(matrix, num_topics=topicsNun, id2word = dictionary, passes=passes)
    #extract topics
    topic = ldamodel.print_topics(num_topics=topicsNun, num_words=5)
   

    
    
    ##Identify the keywords defined in the topics
    hashtags = []
    
    for t in topic:
        for h in t[1].split('+'):    
            hashtags.append(h[h.find('"')+1:h.rfind('"')])
    playload = hashtags_check_emotion (list(set(hashtags)))

    return (playload)





def main(text):
  generateHashtags(text)
  
  
if __name__ == '__main__':
    main()
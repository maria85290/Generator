import pandas as pd
# import nltk

df = pd.read_csv('essays_original_splitted.csv').drop(columns='split')  # removes split column
df = df.replace({'n': 0, 'y': 1})  # turns y/n into binary

df.insert(1, 'year', df['#AUTHID'].apply(lambda id: id[0:4]))  # creates new column with year info
df['#AUTHID'] = df['#AUTHID'].apply(lambda id: id[0:-4])  # removes '.txt' from IDs

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# moved the imports, for readability
from nltk import word_tokenize, pos_tag
from autocorrect import Speller
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import sent_tokenize


def get_wordnet_pos(treebank_tag):
    """
    return WORDNET POS compliance to WORDENT lemmatization (a,n,r,v)
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def treat_data(sentence):
    s_tokens = word_tokenize(sentence)
    spell = Speller("en")
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')

    for i in range(len(s_tokens)):
        # correct the word spelling
        s_tokens[i] = spell(str.lower(s_tokens[i]))

        # postag
    pt = pos_tag(s_tokens)
    word_list = []
    for tag in pt:
        w_temp = lemmatizer.lemmatize(word=tag[0], pos=get_wordnet_pos(tag[1]))
        if w_temp not in stop_words and w_temp.isalnum() and not w_temp.isdigit():
            word_list.append(w_temp)
    return word_list


def text2words(text):
    clean_words = []
    sent_list = sent_tokenize(text)
    for sent in sent_list:
        clean_words += treat_data(sent)
    return clean_words


df.insert(3, 'WORDS', df['TEXT'].apply(text2words))
df.to_csv('out.csv', index=False)
# df.to_json('pretty.json', orient='records')

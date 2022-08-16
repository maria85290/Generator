
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 1


if __name__ == "__main__":
    url = "https://poligrafo.sapo.pt/fact-check/portugal-e-o-pais-da-uniao-europeia-com-mais-emigrantes-espalhados-pelo-mundo"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    print (parser.document)
    print ("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
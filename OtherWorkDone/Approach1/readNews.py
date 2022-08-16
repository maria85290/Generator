'''
This file is responsible for parsing news contained in the url
'''

from unittest import result
from newspaper import Article

def readFromURL(url, resultType):
        article = Article(url)

        try:
            article.download()
            article.parse()
            article.nlp()
      
            if resultType == "text":
                text = article.text
            elif resultType == "summary":
                text = article.summary
            else:
                text = article.title
            return text
        except:
            
            return ""
    

def main(url, resultType): 
    return (readFromURL(url, resultType))
   
 
if __name__ == "__main__": 
	main() 
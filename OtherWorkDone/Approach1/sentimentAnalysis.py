import requests



def sentimentAnalysis(text,lang):
    body = {

        "messages": text,

        "language": lang

        }

    request = requests.post("http://146.59.159.119:9777", json = body)
    return (request.text.encode().decode('unicode-escape') , request.status_code)



def main(text, lang) : 
    return (sentimentAnalysis(text,lang))
 


if __name__ == "__main__": 
    main() 
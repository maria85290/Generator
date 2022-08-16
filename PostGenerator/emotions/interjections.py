
import random
import json

def interjections (evaluation):
    with open('../../corpus/interjections.json') as f:
        interjection = json.load(f)
        if evaluation == "true":
            l = random.choice (interjection["true"])
        else:
            l = random.choice (interjection["fake"])
        return l
 

def main(evaluation):
  interjections(evaluation)
  
  
if __name__ == '__main__':
    main()
'''
Neste modulo pretende-se verificar se um post (em formato de string) tem um formato válido de um microblog:

     1) 0 < número de carateres ≥ 280 
'''

def verify_length(post):
    if len(post)>280:
        return False
    return True
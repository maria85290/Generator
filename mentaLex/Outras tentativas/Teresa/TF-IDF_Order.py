import ast
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

ocean_words = pd.read_csv('out.csv', usecols=['#AUTHID', 'WORDS', 'cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN'],
                          dtype={'cEXT': bool, 'cNEU': bool, 'cAGR': bool, 'cCON': bool, 'cOPN': bool})
ocean_words['WORDS'] = ocean_words['WORDS'].apply(ast.literal_eval)

words = ocean_words['WORDS'].explode().unique().tolist()


def dummy_tokenizer(doc):
    return doc


def tfidf_trait(df, trait, b):
    small_df = df[df[trait] == b]
    tfidf_model = TfidfVectorizer(vocabulary=words, tokenizer=dummy_tokenizer, preprocessor=dummy_tokenizer,
                                  token_pattern=None, analyzer='word')
    fitted = tfidf_model.fit_transform(small_df.WORDS).todense()
    df_tfidf = pd.DataFrame(fitted)
    df_tfidf.columns = sorted(tfidf_model.vocabulary_)
    tfidf_mean = df_tfidf.mean()
    return dict(tfidf_mean)


lexicon = pd.DataFrame(words, columns=['words'])
for trait in ['cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN']:
    for b in [False, True]:
        col_name = '{0}_{1}'.format(trait, b)
        lexicon[col_name] = lexicon['words'].map(tfidf_trait(ocean_words, trait, b))
    col_perc_name = '{0}_perc'.format(trait)
    lexicon[col_perc_name] = (lexicon['{0}_True'.format(trait)] - lexicon['{0}_False'.format(trait)] + 1) / 2

print(lexicon[['words', 'cEXT_perc', 'cNEU_perc', 'cAGR_perc', 'cCON_perc', 'cOPN_perc']])
lexicon.to_csv('lexicon.csv', index=False)

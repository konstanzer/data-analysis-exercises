import pandas as pd
import re
import unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import acquire

def clean(string):
    """Clean text
    """
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
        .encode('ascii','ignore')\
        .decode('utf-8', 'ignore')
    #replace stuff that is not letter, number, or whitespace
    string = re.sub(r"[^\w\s]", '', string).lower()
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string

def tokenize(string):
    """Tokenize text
    """
    tokenizer = ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    return string

def stem(string):
    """Stem text
    """
    snowball = SnowballStemmer(language='english')
    stems = [snowball.stem(word) for word in string.split()]
    stems = ' '.join(stems)
    return stems

def lemmatize(string):
    """Lemmatize text
    """
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    lemmas = ' '.join(lemmas)
    return lemmas

def remove_stopwords(words, extra=[], exclude=[]):
    """Remove stopwords
    Args:
        words: input list
        extra: list of words to keep in output
        exclude: list of words to exclude from output
    Out:
        string
    """
    sw = stopwords.words('english')
    sw = set(sw) - set(exclude)
    sw = sw.union(set(extra))
    filtered_words = [word for word in words.split() if word not in sw]
    return ' '.join(filtered_words)

def process_text(df, content, extra=[], exclude=[]):
    '''Process text and return dataframe
    '''
    df['original']= df[content]  
    df['clean'] = df[content].apply(clean).apply(tokenize)\
                    .apply(lambda x: remove_stopwords(x, extra, exclude))
    df['stemmed']= df['clean'].apply(stem)
    df['lemmatized'] = df['clean'].apply(lemmatize)
    return df

if __name__ == "__main__":
    """Acquire and prepare data from Codeup and Inshorts
    """
    df = process_text(acquire.get_codeup_articles(), 'content')
    print(df.head())
    df = process_text(acquire.get_inshorts_articles(), 'content')
    print(df.head())
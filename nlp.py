from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk import download

from string import punctuation

word_punct_tokenizer = WordPunctTokenizer()
download('stopwords')
swords = stopwords.words('english')

def sentence_wrangler(sentence):
    word_list = word_punct_tokenizer.tokenize(sentence.lower())
    removed_words = []
    result = []
    for word in word_list:
        if word in swords:
            removed_words.append(word)
            continue
        check = False
        for char in word:
            if char in punctuation:
                check = True
                removed_words.append(word)
                break
        if not check: result.append(word)
      
    return result, removed_words


def get_bag_and_tokenize(data, text_col):
    bag = set()
    sentences = []
    for i in range(len(data.index)):
        t = data.iloc[i][text_col]
        try:
            t.encode('ascii')
            words = set(sentence_wrangler(t)[0])
            for word in words:
                if word not in bag:
                    bag.add(word)
            sentences.append(words)
        except UnicodeEncodeError:
            pass
    return frozenset(bag), sentences

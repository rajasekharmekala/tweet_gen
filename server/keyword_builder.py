from nltk.tokenize import TweetTokenizer
# nltk.download()
# nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk import ne_chunk, tree

class KeywordBuilder():

    @staticmethod
    def get_keyword_counts(tweets, maxwords=500):
        dict = {}
        for id, created_at, text  in tweets:
            tokenizer = TweetTokenizer()
            tokens = tokenizer.tokenize(text)
            pos_tags = pos_tag(tokens)
            tagged_tokens = [' '.join(KeywordBuilder.concat_leaves(ne.leaves()) ) for ne in ne_chunk(pos_tags, binary=True) if isinstance(ne, tree.Tree)]
            for token in tagged_tokens:
                token = token.lower()
                dict[token] = dict.get(token, 0)+1
        items = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
        count = 0
        stop_words = set(stopwords.words('english'))
        result = []
        for key, value in items:
            if key  in stop_words or len(key)<=2:
                continue
            count+=1
            if(count>maxwords):
                break
            result.append({"text": key, "value": value})
        return result

    @staticmethod
    def is_proper_noun(pos):
        return pos == 'NNP'

    @staticmethod
    def concat_leaves(leaves):
        return list(x[0] for x in filter(lambda x: KeywordBuilder.is_proper_noun(x[1]),leaves))

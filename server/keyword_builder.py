from nltk.tokenize import TweetTokenizer
# nltk.download('stopwords')
# from wordcloud import WordCloud, ImageColorGenerator
# from PIL import Image
# import matplotlib.pyplot as plt
# import csv

from nltk.corpus import stopwords

class KeywordBuilder():

    @staticmethod
    def get_keyword_counts(tweets, maxwords=500):
        tokenizer = TweetTokenizer()
        dict = {}
        for id, created_at, text  in tweets:
            for token in tokenizer.tokenize(text.lower()):
                dict[token] = dict.get(token, 0)+1
        items = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
        count = 0
        stop_words = set(stopwords.words('english'))
        result = []
        for key, value in items:
            if key  in stop_words or len(key)<2:
                continue
            count+=1
            if(count>maxwords):
                break
            result.append({"text": key, "value": value})
        return result
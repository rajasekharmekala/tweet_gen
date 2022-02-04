from flask import Flask, request
from word_cloud import Worldcloud
from keyword_builder import KeywordBuilder
app = Flask(__name__)
from flask_cors import CORS, cross_origin
# CORS(app, resources={r"/wordcloud/*": {"origins": "*"}})
# two decorators, same function
@app.route('/')
@app.route('/wordcloud')
@cross_origin()
def build_wordcloud():
    screen_name = request.args.get('screen_name')
    dict = {}
    tweets = Worldcloud.get_tweets(screen_name)
    dict["data"] = KeywordBuilder.get_keyword_counts(tweets)
    return dict
    # dict["todler"] = 64
    # dict["mistake"] = 20
    # dict["thought"] = 35
    # dict["bad"] = 50

    # return dict

if __name__ == '__main__':
    app.run(debug=True)
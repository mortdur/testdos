from requests.api import request
import streamlit as st
import requests
import streamlit.components.v1 as components

def TheTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

res = TheTweet("https://twitter.com/FrostedBlakes34/status/1625617524564828174")
#st.write(TheTweet)
components.html(res, height=600)
components.html("<a href="https://twitter.com/intent/tweet?button_hashtag=LoveTwitter&ref_src=twsrc%5Etfw" class="twitter-hashtag-button" data-show-count="false">Tweet #LoveTwitter</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>", width=200, height=200)

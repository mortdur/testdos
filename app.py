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
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("Tumor cerebral"):
    st.text("Aqui podremos predecir si tenemos un tumor y de que tipo")
    
components.html('<a class="twitter-timeline" data-width="250" data-height="450" data-theme="light" href="https://twitter.com/BradleyLJones?ref_src=twsrc%5Etfw">Tweets by BradleyLJones</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')


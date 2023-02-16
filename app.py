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

expander = st.expander("See explanation")
expander.write(\"\"\"
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
\"\"\")

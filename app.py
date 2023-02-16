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
with st.expander("See explanation"):
    st.write(\"\"\"
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    \"\"\")
    components.html(res, height=600)

components.html('<a class="twitter-timeline" data-width="250" data-height="450" data-theme="light" href="https://twitter.com/BradleyLJones?ref_src=twsrc%5Etfw">Tweets by BradleyLJones</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')

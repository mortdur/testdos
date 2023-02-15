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
components.html(res,height=600)
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I think about Eric Andre having Tyler The Creator on his show a lot <a href="https://t.co/0IEknST6oM">pic.twitter.com/0IEknST6oM</a></p>&mdash; Blake Garman (@FrostedBlakes34) <a href="https://twitter.com/FrostedBlakes34/status/1625617524564828174?ref_src=twsrc%5Etfw">February 14, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

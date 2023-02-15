from requests.api import request
import streamlit as st
import requests
import streamlit.components.v1 as components

def TheTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res
input = "https://twitter.com/FrostedBlakes34/status/1625617524564828174"
res = TheTweet(input)
#st.write(TheTweet)
components.html(res, height=600)

from request.api import request
import streamlit as st
import requests
import streamlit.components.v1 as components

def TheTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(s)
    response = requests.get(api)
    res = reponse.json()["html"]
    return res
TheTweet("https://twitter.com/ark9451/status/1579814253070266375")
#st.write(TheTweet)
components.html(TheTweet, height=600)

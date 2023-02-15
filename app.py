from requests.api import request
import streamlit as st
import requests
import streamlit.components.v1 as components

class Tweet(object):
    def __init__(self,tweet_url):
        api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
        response = requests.get(api)
        res = response.json()["html"]
        return 
    res = tweet_url

    def ajuste(self):
        components.html(res, height=600)
        
TheTweet = Tweet("https://twitter.com/ark9451/status/1579814253070266375")

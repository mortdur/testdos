from requests.api import request
import streamlit as st
import requests
import streamlit.components.v1 as components

def TheTweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

col1, col2 = st.columns([3, 1])

col1.subheader("A wide column with a chart")
col1.res = TheTweet("https://twitter.com/FrostedBlakes34/status/1625617524564828174")

col2.subheader("A narrow column with the data")
with st.expander("Tumor cerebral"):
    st.text("Aqui podremos predecir si tenemos un tumor y de que tipo")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("Tumor cerebral"):
    st.text("Aqui podremos predecir si tenemos un tumor y de que tipo")
    

import streamlit as st
import scrapy

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    start_urls = [
        'https://twitter.com/search?q=%23yourhashtag&src=typd'
    ]

    def parse(self, response):
        for tweet in response.css('div.tweet'):
            yield {
                'username': tweet.css('span.username::text').get(),
                'tweet': tweet.css('p.tweet-text::text').get(),
                'time': tweet.css('span._timestamp::attr(data-time)').get()
            }
tab1= st.tabs(["Una entrada"])
with tab1:
    st.slider("Peso w0:",0.0, 5.0)

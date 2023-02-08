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
 tab1, tab2 = st.tabs(["Una entrada", "Dos entradas"])
 next_page = response.css('div.stream-container div.stream > div.stream-item:last-child > div.stream-item > div.tweet:last-child > div.tweet-context a.js-next-link::attr(href)').get()
   if next_page is not None:
     with tab1:
     yield response.follow(next_page, self.parse)
    
 with tab2:
    st.slider("Peso w0:",0.0, 5.0)
    

import requests
import streamlit.components.v1 as components

class Tweet(object):
	def __init__(self, tid, embed_str=False):
		if not embed_str:
			try:
				# Use Twitter's oEmbed API
				# https://dev.twitter.com/web/embedded-tweets
				api = 'https://publish.twitter.com/oembed?url=https://twitter.com/XXX/status/'+tid
				response = requests.get(api)
				self.text = response.json()["html"]
			except:
				return "<blockquote class='missing'>This tweet is no longer available.</blockquote>"
		else:
			self.text = tid

	def _repr_html_(self):
		return self.text

	def component(self):
		return components.html(self.text, height=600)

def top_daily_tweets(df):
	df = df.sort_values(['Followers'], ascending=False).head(10)
	return df

top_daily_tweets = top_daily_tweets(data)

with st.expander("Twitter feed", expanded=True):             
	st.subheader("Most influential tweets")
	for i in range(len(top_daily_tweets)):
		t = Tweet(top_daily_tweets.iloc[i]['tweet_id']).component()

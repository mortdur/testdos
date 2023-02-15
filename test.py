class Tweet(object):
	def __init__(self, tid, embed_str=False):
		if not embed_str:
			try:
				# Use Twitter's oEmbed API
				# https://dev.twitter.com/web/embedded-tweets
				api = 'https://publish.twitter.com/oembed?url={}'.format(s)
				response = requests.get(api)
				self.text = response.json()["html"]
			except:
				return "<blockquote class='missing'>This tweet is no longer available.</blockquote>"
		else:
			self.text = tid

	def _repr_html_(self):
		return self.text

st.write('''
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FOReillyMedja%2Fstatus%2F901048172738482176)](https://twitter.com/OReillyMedja/status/901048172738482176)
''')

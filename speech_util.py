import pyttsx # read about the API
import feedparser


class SpeechUtils(object):

    def __init__(self):
        self.engine = pyttsx.init()
        self.engine.setProperty('rate', 150)
        self.voices = self.engine.getProperty('voices')
        self.uk_feed_url = 'http://feeds.bbci.co.uk/news/uk/rss.xml?edition' \
                           '=uk'

    def read_the_given_text(self, passed_text):
        self.engine.say(passed_text)

    def read_rss_feed(self, url=None):
        if not url:
           url = self.uk_feed_url
        raw_feed = feedparser.parse(url)
        for feed in raw_feed['entries']:
            feed_title = feed['title']
            feed_summary = feed['summary']
            read_feed = 'The feed title is %s. The feed is about: %s' % (
                feed_title, feed_summary)
            self.engine.say(read_feed)
        self.engine.runAndWait()

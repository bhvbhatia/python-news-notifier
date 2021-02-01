# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import feedparser
from plyer import notification
import time
def parseFeed():
    f = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
    for newsitem in f['items']:
        notification.notify(
            title=newsitem['title'],
            message=str(newsitem['summary']),
            timeout=20000,
            app_icon="News.ico"
        )
    time.sleep(60)

if __name__ == '__main__':
    parseFeed()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

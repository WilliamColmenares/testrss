from .models import News
from celery import shared_task
import feedparser
import re


@shared_task()
def get_news():
    rssnews = feedparser.parse('https://news.google.com/rss')  # Google's rss
    for i in range(len(rssnews['entities'])):
        news_id = int(rssnews['entities'][i].id)
        try:
            News.objects.get(id=news_id)
        except News.DoesNotExist:
            News.objects.create(
                id=news_id,
                title=rssnews['entities'][i].title,
                # Here I user this regex to remove some html tags
                content=re.sub('<[^<]+?>', '', rssnews['entries'][0].summary))

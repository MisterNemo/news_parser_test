import requests
from bs4 import BeautifulSoup as bsoup

from api.models import Post


def news_parse():
    try:
        post = Post.objects.latest('news_id')
    except Post.DoesNotExist:
        post_news_id = None
    else:
        post_news_id = post.news_id

    URL = "https://news.ycombinator.com/"
    request = requests.get(url=URL + 'newest')
    soup = bsoup(request.content, 'html.parser')

    news_posts = soup.find_all('tr', attrs={'class': 'athing'})

    for news_post in news_posts:
        news_id = int(news_post['id'])
        if news_id != post_news_id:
            news_data = news_post.find('a', attrs={'class': 'storylink'})
            news_title = news_data.text
            news_url = news_data['href']
            Post.objects.create(title=news_title, url=news_url, news_id=news_id)
        else:
            break

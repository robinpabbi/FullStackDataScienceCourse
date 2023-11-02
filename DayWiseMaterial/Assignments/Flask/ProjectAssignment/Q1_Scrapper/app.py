from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

from model import ScrappedNews

app = Flask(__name__)

@app.route('/')
def index():
    # Accessing TOI webpage disguised as a browser
    webpage = requests.get('https://timesofindia.indiatimes.com/').text

    soup = BeautifulSoup(webpage, 'lxml')
    news = []

    for i in soup.find_all('div', class_='col_l_6'):
        figcaption = i.find('figcaption')
        if figcaption is not None:
            # Finding news headline as well its corresponding link
            link_news = i.find('a').get("href")
            text_news = figcaption.text.strip()
            news_scrpd = ScrappedNews(text_news, link_news)
            news.append(news_scrpd)
    return render_template('index.html', news_headlines=news)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)

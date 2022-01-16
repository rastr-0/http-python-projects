import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.ukr.net/news/kharkiv.html'
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        all_news = soup.findAll('a', 'im-tl_a')
        all_time = soup.findAll('time', 'im-tm')
        all_authors = soup.findAll('div', 'im-pr')
        result_news = []
        result_time = []
        post_author = []
        for data_news in all_news:
            result_news.append(data_news.text)
        for data_time in all_time:
            result_time.append(data_time.text)
        for data_authors in all_authors:
            post_author.append(data_authors.text)
        i = 0
        while i < len(result_time):
            print(result_time[i] + ' ' + result_news[i] + ' -- ' + post_author[i])
            i += 1


if __name__ == '__main__':
    main()

import pandas as pd
from app_store_scraper import AppStore
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import urllib.request



apps_df = pd.read_csv('apps.csv', names=['app_id', 'app_name'], header=0)
apps_df.head()

def Crawl_app(app_info, app):
    total_rating = 0
    for i, review in enumerate(app):
        total_rating += int(review['rating'])

    average_rate_from_reviews = total_rating / app_info.reviews_count
    app_rate = str.split(soup.find("figure", {"class": "we-star-rating ember-view"})['aria-label'])[0]
    response = urllib.request.urlopen(app_info.url).read()
    soup = BeautifulSoup(response)
    genre = str.split(soup.find("li", {"class": "inline-list__item"}).text)[-1]
    app_type = soup.find('li', {'app-header__list__item--price'}).text
    tple = (app_info.app_id, app_info.app_name, app_rate, average_rate_from_reviews, app_info.url, genre, app_type)

    return tple


def Crawl_appsList(l):
    dataTable = []
    for i, app in enumerate(l):
        try:
            application = AppStore(country="eg", app_name=app)
            application.review()
            tupl = Crawl_app(application, application.reviews)
            dataTable.append(tupl)
        except:
            print("Couldn't found App: ", app, "\nCheck the application name again.")
            continue

    return dataTable


df = apps_df['app_name'].values
df = Crawl_appsList(df)
data = pd.DataFrame(data=df,
                    columns=['ID', 'Name', 'Overall Rate',
                             'Average Rate From Reviews', 'URL',
                             'Genre', 'Type'])
data.head()
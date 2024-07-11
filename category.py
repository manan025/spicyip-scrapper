import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

"""
1. Run ```pip install -r requirements.txt``` to install all required packages.
2. Change category (in function scrapper) to the category you are scrapping.
3. Change the link in the scrapper function to the category you are scrapping.
4. Change the number of pages you will scrap.
5. Run
"""

try:
    open('data.csv', 'r').close()
except FileNotFoundError:
    file = open('data.csv', 'w')
    csv.writer(file).writerow(['category', 'title', 'date', 'link'])
    file.close()


# categories = ["copyright", "trademark"]  # convert tags to lower case when matching
# TODO: use categories


def scrapper(page):
    """
    span class published -> date
    a class ast-button -> href link
    span inside a class screen-reader-text -> title
    ---
    :param page: page number to scrap
    :return: list of articles in the category
    """
    url = 'https://spicyip.com/category/copyrights/page/' + str(page)
    category = "copyright"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    lst = []
    for article in articles:
        x = [category]
        title = article.find('span', class_='screen-reader-text')
        date_p = article.find('span', class_='published')
        link = article.find('a', class_='ast-button')

        try:
            x.append(title.text)
            x.append(date_p.text)
            x.append(link['href'])
            lst.append(x)
        except:
            pass
    return lst


end_page = 2
for i in range(1, end_page + 1):
    lst = scrapper(i)
    file = open('data.csv', 'a+')
    reader = csv.reader(file)
    writer = csv.writer(file)

    df = pd.read_csv('data.csv')
    links = df['link'].tolist()
    for row in lst:
        if row[3] in links:
            idx = links.index(row[3])
            df.at[idx, 'category'] = df.at[idx, 'category'] + ' ', row[0]
            df.to_csv('data.csv', index=False)
        else:
            writer.writerow(row)




    file.close()
    print('Page ' + str(i) + ' has been scrapped')

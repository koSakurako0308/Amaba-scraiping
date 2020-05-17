import requests
import datetime
import re
import pandas as pd
from bs4 import BeautifulSoup


def amaba(csvload,page,group,word):
    screan_w(page, group, csvload)
    print("{} test".format(screan_w(page, group, csvload)))
    screan_r(csvload, word)

def screan_w(i, top_page,csvload):
    title_date = []
    img_data = []
    day_count = []
    df = pd.DataFrame()
    time = 0
    for page in range(i):
        count = 0
        page_url = "{}/page-{}.html".format(top_page, page+1)
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, features="html.parser")
        img_tags = soup.find_all("img", src=re.compile(
            'https://stat.ameba.jp/user_images/'))
        name_tags = soup.find_all("a", class_="skinArticleTitle")[0].text
        for img_tag in img_tags:
            count += 1
            img_url = img_tag.get("src")
            day_count.append(count)
            title_date.append(name_tags)
            img_data.append(img_url)
            time += 1
    df["daycount"] = day_count
    df["title"] = title_date
    df["img"] = img_data
    df.to_csv("{}/log.csv".format(csvload), encoding='utf_8_sig')
    return time


def screan_r(csvload, word):
    df = pd.DataFrame()
    df = pd.read_csv("{}/log.csv".format(csvload), index_col=0)
    df = df[df['title'].str.contains(word)]
    img_data = df["img"]
    i = 0
    title = []
    daycount = []
    for title_data in df['title']:
        title.append(title_data)
    for daycount_data in df['daycount']:
        daycount.append(daycount_data)
    for img_url in img_data:
        r = requests.get(img_url)
        file_name = "{}-{}".format(title[i],daycount[i])
        with open('{}/{}.jpg'.format(csvload, file_name), 'wb') as file:
           file.write(r.content)
        i += 1

if __name__ == '__main__':
    amaba(csvload,page,group,word)
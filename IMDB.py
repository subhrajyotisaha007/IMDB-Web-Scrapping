import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/88.0.4324.182 Safari/537.36"}
data = requests.get("https://www.imdb.com/find/?s=ep&q=thriller&ref_=nv_sr_sm",headers=headers)

soup = BeautifulSoup(data.content,'html.parser')

movies = soup.find('ul',{'role':'presentation'})

rows = movies.findAll('li',{'class':'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result'})
for row in rows:
    row_data = row.findAll('div',{'class':'ipc-metadata-list-summary-item__c'})
    for value_data in row_data:
        title_value = value_data.find('div',{'class':'ipc-metadata-list-summary-item__tc'})
        title = title_value.find('a',{'role':'button'}).text
        print(title)
        print('genre', "-->", end=' ')
        suburl = title_value.find('a')['href']
        # print(suburl)
        actualurl = "https://www.imdb.com" + suburl
        subget_resp = sub_resp = requests.get(actualurl, headers=headers)
        subget_htmldata = BeautifulSoup(subget_resp.content, 'html.parser')
        # print(subget_htmldata.prettify())
        genre_row1 = subget_htmldata.find('div', {"class": "ipc-chip-list__scroller"})
        for value_genre in genre_row1:
            genre11 = value_genre.findAll('span', {"class": "ipc-chip__text"})
            for genre in genre11:
                print(genre.text, end=" ")
    print('\n')
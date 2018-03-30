import bs4
import webbrowser
import requests
import logging
from fake_useragent import UserAgent
url = 'https://www.google.co.il/search?q=eminem+twitter'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

# header variable
headers = { 'User-Agent' : user_agent }


query = requests.get('https://www.google.com/search?q=yasser',headers=headers)
html_query = open('html_query.txt','r+',encoding='utf-8')
html_query.write(query.text)

html_query.close()

html_query = open('html_query.txt','r',encoding='utf-8')
#print(html_query.read())
google_result = bs4.BeautifulSoup(html_query.read(),'lxml')
another_way = google_result.select('.r a')
print(another_way[0])
print(another_way[0].get('href'))
top = google_result.find_all('cite', attrs={'class': 'iUh30'})
for url in top:
    print(url.text)

import requests
import shutil
import bs4
import os
url = 'https://www.google.co.il/search?q=eminem+twitter'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

# header variable
headers = { 'User-Agent' : user_agent }


for number in range(1,1970):
    htmlpage = requests.get('https://xkcd.com/{0}/'.format(number))
    page = htmlpage.text
    content = bs4.BeautifulSoup(page,'lxml')
    url = content.select('.box img')
    url = url[0].get('src')
    print(url)
    image = requests.get('https:{0}'.format(url),stream=True)
    nameUrl = str(url).split('/')[-1]
    print(nameUrl)
    try:
        os.mkdir('xkcdfolder')
    except:
        pass
    with open('xkcdfolder//{0}'.format(nameUrl),'wb') as out_file:
        shutil.copyfileobj(image.raw,out_file)
    del image


import requests
import pprint
import shutil
import bs4
import os
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

t1 = time.time()


def replace_img_small_to_big(url):

    if url.find('50x48') != -1:
        return ''
    url = url.replace('small_image','image')
    url = url.replace('170x165','720x680')
    return url

#replace_img_small_to_big('http://www.othaimmarkets.com/media/catalog/product/cache/4/small_image/170x165/9df78eab33525d08d6e5fb8d27136e95/4/3/437550_0.jpg')


def main():

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.3ci6'
    headers = { 'User-Agent' : user_agent,
                'Cookie' : 'frontend=4fc2a2f665ab20702f316fad0efa83c1; __utma=64338161.12960362.1522093959.1522093959.1522093959.1; __utmb=64338161.11.10.1522093959; __utmc=64338161; __utmz=64338161.1522093959.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); cookie_country=sa; __ar_v4=QEZYSDRFGVA5PHP46IA43E%3A20180325%3A4%7CMOUPUUQ7V5ETTP5ZPQDOAT%3A20180325%3A4%7CBPHNGPC7FNDD3CBVQ6LP6Q%3A20180325%3A4'}
    url = 'http://www.othaimmarkets.com/fresh-and-bakery/bakery.html'
    # header variable
    main_html = requests.get(url,headers=headers)
    main_html = main_html.text
    main_html = bs4.BeautifulSoup(main_html,'lxml')

    menues = main_html.findAll('a', attrs={"class": ''})

    print('---------------')



    file = open('C:\\Users\\xl7\\Desktop\\html.txt','w+',encoding='utf-8')
    urls = open('urls.txt','r').read().split('\n')
    for url in urls:
        exist = False
        for i in range(1,10):

            local_url = '{0}?p={1}'.format(url,i)
            logging.info('url = {}'.format(local_url))
            htmlpage = requests.get(local_url,headers=headers)
            page = htmlpage.text
            file.write(page)
            file.write('-----------------------------')
            content = bs4.BeautifulSoup(page,'lxml')
            #print(htmlpage.text)

            whole_div = content.findAll('div', attrs={'class': 'span2 product'})
            products = {}

            #logging.info('is the url? ' + prices[0].get('src'))
            #logging.info('how many images:  {}'.format(len(images)))
            for element in whole_div:
                image = element.find('img', attrs= {'class': 'product-retina'})
                price = element.find('span', attrs= {'class': 'price'})
                price = price.get_text()
                big_image_url = replace_img_small_to_big(image.get('src'))
                if big_image_url == '':
                    continue
                name = image.get('alt')
                name = name.replace('/','')
                name = name.replace('*','')
                name = name.replace('.','')
                print('Product Name: {}'.format(name), '\nPrice: {}'.format(price), '\nimage_url {}'.format(big_image_url))
                products[name] = [url,price]
                image_url = requests.get(big_image_url, stream=True)
                os.makedirs('alothaim', exist_ok=True)
                os.makedirs('alothaim//{0}'.format(content.title.string), exist_ok = True)
                path = 'alothaim//{0}//{1}.jpg'.format(content.title.string,name)

                if os.path.isfile(path):
                    exist = True
                    break
                with open(path , 'wb') as raw_image:
                    shutil.copyfileobj(image_url.raw,raw_image)
                print('---------')
            print('*****************************************************************')
            #print(name)
            print('*****************************************************************')

    t2 = time.time()
    print(t2 - t1)









main()






'''
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
'''
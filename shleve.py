import shelve

shelfFile = shelve.open('mydata')
cat = ['Yasser','Abdullah','Firas']
shelfFile['cat'] = cat
shelfFile.close()

import pprint
people = [{'name': 'Yasser', 'size':'43'}]
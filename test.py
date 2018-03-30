import time
string = 'http://www.othaimmarkets.com/grocery/oils-ghee.html'
print(string.split('/')[-2])
strr = '  aaa   '
print(strr.strip())
import re
string = "aagd-/\\\* \ ب\س>?\>>يدa+*-"
string = re.sub('-','_',string)
print(re.sub((r'[/\\"*\-+|*?:<>]'), '',string))


import csv
'''
file = open('test.csv',newline='')
test_reader = csv.reader(file, quotechar= '|')
for row in test_reader:
    print(row)
    
file.close()
'''
with open ('test.csv','w',newline='') as csvfile:
    fieldnames = ['#','ITEMS','PRICE']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'#':'1', 'ITEMS':'MILfsdfsd    ,fas fdsK', 'PRICE':'321'})
    writer.writerow({'#':'1', 'ITEMS':'MILfsdfsd    ,fas fdsK', 'PRICE':'321'})


def addition(number1,number2):
    print(number1)
    print(number2)
import os


list = ['C:\\','Users','xl7','Automatethebroingstuff','image.jpg']
print(os.path.join(*list))
print(*list)
lista = [1,3]
addition(*lista)

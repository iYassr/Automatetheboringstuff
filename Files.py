import os

totalSize = 0
path = 'C:\\windows\\System32'
for fileName in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path,fileName))


print(totalSize)


print (os.path.join('C:\\','Windows','System32'))

os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)


"""        Files        """

textFile = open('C:\\Users\\xl7\\Desktop\\text.txt','a')
textFile.write('NOT HELLO WORLD')

#print(textFile.read())

print(os.path.join('C:\\','windows'))





























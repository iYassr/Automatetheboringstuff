import zipfile

newZip = zipfile.ZipFile('new.zip','w')
file = open('spam.txt','w')
file.write('hello world')
file.close()
newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


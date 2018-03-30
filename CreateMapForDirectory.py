import CreateMapForDirectory,os
import sys
import argparse

# -*- coding: utf-8 -*-

parser = argparse.ArgumentParser(description='simple program to build a tree out of your directory')
parser.add_argument('-d','-directory',help='directory to be traversed',required=True)
args = parser.parse_args()
print (args.d)


file = open('FileSystemMap.txt','w',encoding="utf-8")

try:
    for path, subFolders, fileNames in os.walk(args.d):
        print('The current folder is ' + path)
        folderNameOnly = str(path).split('//')
        file.write(folderNameOnly[-1] + ': \n')
        for subFolder in subFolders:
            file.write('    ' + subFolder + ': \n')
            print('     Subfolder of ' + path + ': ' + subFolder)
        for fileName in fileNames:
            file.write('        ' + fileName + ': \n')
            print('         ' + path + ': ' + fileName)

        print('')

except:
    exception = sys.exc_info()
    print(exception)
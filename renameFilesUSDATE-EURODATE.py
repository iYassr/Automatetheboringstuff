import shutil, os, re




absWoringDir = os.path.abspath(os.path.join(os.environ["HOMEPATH"], "Desktop"))
myDir = '%s\\myDir' % (absWoringDir)

#os.rmdir(('%s\\myDir') % (absWoringDir))
try:
    os.mkdir(myDir)
    print('created')
except:
    print('already created brov')

for i in range(10):
    #file = open('%s//file%s' % (myDir,i),'w')
    # file.write('%s' % (i))
    shutil.move('%s//file%s' % (myDir,i), '%s//notfile%s' % (myDir,i))



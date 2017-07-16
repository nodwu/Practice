#encoding:utf-8
import os
import time

fcount=open('/home/count.txt')
lastCount=int(fcount.read()[0])
#nextCount=int(lastCount) + 1
#print nextCount
print "last count is %s line" % lastCount
fcount.close()

resf=open('/home/res.txt','wb')
resf.truncate()
resf.close()

ftime=time.strftime('%Y%m%d')
filepath = '/home/' + ftime + '.txt'
print filepath
if os.path.exists(filepath):
    print 'The file is %s %s ' % (filepath,"********")
    fileContent=open(filepath,'r')
    newContent=fileContent.readlines()[lastCount:]
    print "new countent is %s" % newContent
    for i in newContent:
        print "i is %s and position is %s\n" % (i,newContent.index(i))
        if 'err' in i:
            newCount=newContent.index(i) + 1 + lastCount
            fcount=open('/home/count.txt','w')
            fcount.write(str(newCount))
            fcount.close()
            resf=open('/home/res.txt','a+')
            resf.write(i)
            resf.close()
    fileContent.close()
    

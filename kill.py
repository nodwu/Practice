import commands

'''
commands.getstatusoutput(cmd)返回一个元组（status，output）
status代表的shell命令的返回状态，如果成功的话是0；output是shell的返回的结果
'''
res=commands.getstatusoutput('ps -ef|grep 1.sh|grep -v grep')
if res[0] == 0:
    pid=res[1].split()[1]
    print "PID is %s" % pid
    kill=commands.getstatusoutput('kill -9 %s' % pid)
    if kill[0]==0:
        print "kill success"
else:
    print "Not found res is %s" % res[1]
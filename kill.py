import commands

'''
commands.getstatusoutput(cmd)����һ��Ԫ�飨status��output��
status�����shell����ķ���״̬������ɹ��Ļ���0��output��shell�ķ��صĽ��
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
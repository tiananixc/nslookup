#coding:utf-8
import time
from module_caiji import caiji   #调用py文件里面的caiji
baiduuv=open("niuzhan_uv.csv",'a')

caiji=caiji()

i=1
ii=1

while i==1:
	htm=caiji.html('http://zhanzhang.baidu.com/act/lot/sitelist')
	if 'error' in htm:
		print htm
	if htm != 'error':
		baiduuv.writelines(htm+'\n')
		time.sleep(2)
		print u'第'+`ii`+u'个'
		ii+=1



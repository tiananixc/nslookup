#coding:utf-8
from module_caiji import *
uv=open('niuzhan_uv.csv','r').read()
new_uv=open('uv.csv','w')
caiji=caiji()
print uv
ll=caiji.res(uv, r'"url":"http:\\/\\/([\S\.\S\.\S]*?)\\/","value":"[\s\S]*?","clicks":"(\d+?)"')
print type(ll)

for u in caiji.res(uv, r'"url":"http:\\/\\/([\S\.\S\.\S]*?)\\/","value":"[\s\S]*?","clicks":"(\d+?)"'):
	if 'value' not in u[0] :
		print ','.join(u)
		new_uv.writelines(','.join(u)+"\n")

	







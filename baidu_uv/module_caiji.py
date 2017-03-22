#coding:utf-8
import pycurl,re,StringIO,chardet

class caiji:

	#打开网页  url：网页URL  res：正则表达式
	def html(self,url):
		try:
			b=StringIO.StringIO()
			c=pycurl.Curl()
			# head=['Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			# 'Accept-Encoding:gzip,deflate,sdch',
			# 'Accept-Language:zh-CN,zh;q=0.8',
			# 'User-Agent:Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36']
			c.setopt(pycurl.URL,url) #打开URL
			c.setopt(pycurl.FOLLOWLOCATION,2) #允许跟踪来源，有参数：1和2
			c.setopt(pycurl.MAXREDIRS,1) #最大重定向次数，0表示不重定向
			c.setopt(pycurl.CONNECTTIMEOUT,60) #链接超时
			c.setopt(pycurl.TIMEOUT,60)  #下载超时
			#c.setopt(pycurl.HTTPHEADER,head)   #head中的数据类型声明
			cookie='''
			bdshare_firstime=1382711241223; prompt_diliver=1; pagesize=50; kw-pagesize=100; user-setting-click-times=0%2C5; BAIDUID=2C5A522E26A6FFAF7317A5D9A8670BF4:FG=1; mobile_pagesize=50; BDUSS=Up6Z2pTM255bExHWHhOaTdpR1lwcUlmQXpZWWdacDZCbHp2SlpzcHNPeUU3TGRUQVFBQUFBJCQAAAAAAAAAAAEAAACGh~oUs72w1Mzsz8JfeXUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIRfkFOEX5BTV; NBID=65D13CAE3DDC9011C40C56A6419BC2E9:FG=1; cflag=65535%3A1; SITEMAPSESSID=upvja3kfi1oo6vkobqlichtq13; Hm_lvt_031f28a54d603d47eb69f579fb3198a0=1401975868,1402150759,1402586947,1402655302; Hm_lpvt_031f28a54d603d47eb69f579fb3198a0=1402655330; H_PS_PSSID=7016_1445_5225_6995_6506_7057_7037_4760_6017_6999_6931_6983_7106
			'''
			c.setopt(pycurl.COOKIEFILE, cookie)
			c.setopt(pycurl.USERAGENT,'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36')
			#pycurl.USERAGENT  模拟浏览器
			c.setopt(pycurl.WRITEFUNCTION, b.write)  #回调写入字符串缓存
			c.perform() #执行上述访问网址的操作
			# print c.getinfo(pycurl.HTTP_CODE)
			c.close()
			html=b.getvalue()   #读取b中的数据
			return html
		except:
			return 'error'


    #下载图片   pic：图片名   url：图片地址  path图片路径
	def dowImage(self,pic,url,path):

		d = pycurl.Curl()
		d.setopt(pycurl.URL, url)
		pics=path+pic   # 'f:/py/caiji/tailing/image/'+pic 下载的文件保存到image，这里的image必须手动创建，否则报错
		f = open(pics, 'wb')     #c创建一个文件
		d.setopt(pycurl.WRITEFUNCTION, f.write)
		d.perform()
		print pic+u'下载成功'
		d.close()

	#正则表达式提取信息   html：html方法返回的结果，res：正则表达式
	def res(self,html,res):  #正则
		zz=re.compile(res)
		htm=zz.findall(html)
        print type(htm)
        htm=set(htm)
        return htm
        c.close()

	#获取页面编码，html：方法html返回的值
	def chardet(self,html):
		htmchr=chardet.detect(html)
		return htmchr




	# 	htm=b.getvalue()   #读取b中的数据
	# htmchr = chardet.detect(htm)
	# typeEncode = sys.getfilesystemencoding()#系统默认编码
	# infoencode = chardet.detect(htm).get('encoding','utf-8')#通过第3方模块来自动提取网页的编码
	# htm = htm.decode(infoencode,'ignore').encode(typeEncode)#先转换成unicode编码，然后转换系统编码输出



# -*-coding:UTF-8-*- 
import scrapy,random,sys,time,os

class Spider(scrapy.Spider):
    name = "yhd"
    allowed_domains = ["yhd.com"]
    f = open('file/urllist.txt','r')

    start_urls = f.readlines()
    t = time.strftime('%Y年%m月%d日')
    ft = time.strftime('%Y%m%d')
    
    if not os.path.exists('D:/scrapy/'+ft):
        os.mkdir('D:/scrapy/'+ft)
    else:
        print('File Exists')

    # if os.path.exists('url.txt'):
    #     os.remove('url.txt')

    def parse(self, response):
    	print response.url
    	html = response
        cats = html.xpath('//h1/text()').extract()[0]
        gettext = ''
        tcc = city+cats.strip()+'\n'
        gettext += tcc 
        itemss = html.xpath('//*[@id="JlistItems"]')
        items = itemss.xpath('li[@class="item"]')
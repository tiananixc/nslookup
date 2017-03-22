# -*-coding:UTF-8-*- 
import scrapy,random,sys,time,os
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider(scrapy.Spider):
    name = "yhdlist"
    allowed_domains = ["yhd.com"]
    f = open('file/urllist.txt','r')

    start_urls = f.readlines()
    global ft
    t = time.strftime('%Y年%m月%d日')
    ft = time.strftime('%Y%m%d')
    
    if not os.path.exists('D:/scrapy/'+ft):
        os.mkdir('D:/scrapy/'+ft)
    else:
        print('File Exists')

    # if os.path.exists('url.txt'):
    #     os.remove('url.txt')

    def parse(self, response):
    	yhdurl=response.url
        print yhdurl
    	html = response
        cats = html.xpath('//input[@id="choosed_brand_names"]/@value').extract()[0]
        gettext = ''
        tcc = cats.strip()
        gettext += tcc+'价格表：\n'
        itemss = html.xpath('//*[@id="itemSearchList"]')
        #print len(itemss)
        items = itemss.xpath('div[@class="mod_search_pro"]')
        totaln=len(items)
        #gettext=itemss.extract()[0]
        #totaln = html.xpath('//*[@class="total"]/em/text()').extract()[0]
        if totaln>0 and totaln<=10:
            randnl = range(1,totaln)
        elif totaln > 10 and totaln <=25:            
            clnn = range(1,totaln)
            crnum = random.randint(6,12)
            randnl = random.sample(clnn, crnum)
        else :           
            clnn = range(1,25)
            crnum = random.randint(6,12)
            randnl = random.sample(clnn, crnum)
        global j
        j = 0
        for xx,item in enumerate(items,1):            
            for xii in randnl:                
                if xii == xx :
                    j+=1
                    titleitem = item.xpath('./div/p[@class="proName clearfix"]/a/text()').extract()[0]
                    price = item.xpath('.//p[@class="proPrice"]/em/@yhdprice').extract()[0]
                    #print '--------'
                    #print price
                    itemcons = str(j)+'、'+titleitem.strip()+"  价格：￥"+str(price)+'\n'
                    gettext +=itemcons

        filename = 'D:/scrapy/'+ft+'/'+cats.strip().replace('/','')+'.txt'
        f = open(filename,'a')
        f.write(gettext)
        f.close()
        time.sleep(5)
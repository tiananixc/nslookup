#!--encode:utf-8--
import lxml.etree as etree
import requests,sys,re
import socket,os,urllib2

socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')
def getHTml(url):
    #host = search('^([^/]*?)/',re.sub(r'(https|http)://','',url))
    print url,'432'
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; lsv=globalTjs_97273d6-wwwTcss_8eba1c3-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_eabc62a-framejs_902a6d8-globalBjs_2d41ef9-sugjs_97bfd68-wwwjs_8d1160b; MSA_WH=1433_772; BAIDUID=E9B0B6A35D4ABC6ED4891FCC0FD085BD:FG=1; plus_cv=1::m:2a9fb36a; H_WISE_SIDS=107504_106305_100040_100100_109550_104341_107937_108437_109700_109794_107961_108453_109737_109558_109506_110022_107895_107917_109683_109588_110072_107318_107300_107242_100457; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; rsv_jmp_slow=1474644236473; sug=3; sugstore=1; ORIGIN=0; bdime=21110; H_PS_645EC=60efFRJ1dM8ial205oBcDuRmtLgH3Q6NaRzxDuIkbMkGVXNSHmXBfW0GZL4l5pnj; BD_UPN=123253; BD_CK_SAM=1; BDSVRTM=110; H_PS_PSSID=17947",
        "Host":'www.jiuxian.com',
        "Pragma":"no-cache",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        }
    html = requests.get(url,headers=headers,timeout=30)
    #print html.content
    return html.content
def getdomain(url):
    reg = r'^https?://([a-z0-9-.]+)[/?]?'
    m = re.match(reg, url)
    uri = m.groups()[0] if m else ''
    link = uri[uri.find('.', 0, uri.rfind('.')) + 1:]
    return uri,link

def ismake(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print 'file making'
def getprice(url):
    exurl=exurl.strip()
    id = re.search('goods-(.*?).html',exurl).group(1)
    url="http://act.jiuxian.com/act/selectPricebypids.htm?ids=%s,&callback=handleListPrice&handleListPrice=jQuery16203082127552865588_1474970119762&_=1474970120046"% id
    req = urllib2.Request(url)  #
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    r = urllib2.urlopen(req)
    html1 = r.read()
    html=html1.replace('handleListPrice(\'','').replace('\')','')
    #print html
    hdict=eval(html)
    getdata=hdict['data']
    #print getdata

    for v in getdata.values():
        price=v['np']
    return price

website=['http://www.jiuxian.com/goods-1521.html','http://www.jiuxian.com/goods-5674.html']
#f=open('frendlink.txt','w')
for index,s in enumerate(website,1):
    #ismake('frendlink'+str(index)+'.txt')
    #f=open('frendlink'+str(index)+'.txt','w')

    jprice=getprice(s)
    #cl,dl=getdomain(ss)
    #wl=[]
    try:
        html = getHTml(ss)
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
        rt = page.xpath("//span[@class='d-cur']/text()")[0]
        print rt,jprice
        #print html
    except Exception,e:
        print 'website is broken',e
        continue


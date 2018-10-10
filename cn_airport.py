# -*- coding: utf-8 -*-

#from urllib import request,parse,error,response
#from bs4 import BeautifulSoup
#import requests
import json
from urllib import request

#url = 'http://www.umetrip.com/mskyweb/fs/fa.do?dep=DLC&arr=PEK&date=2018-10-03&channel='
# 从航旅纵横 爬取机场信息： 机场名，城市，拼音，三字码等
url = 'http://www.umetrip.com/js/citiesData.js'
req = request.Request(url)
res = request.urlopen(req)
html = res.read().decode()    #爬去的信息问string类型
html =  html[12:]             #将values信息保留
#print(html)
citis = json.loads(html)      #将string信息转为json（list类型）
print(type(citis))
#for city in citis:
#    if city['pinyin'] != '':
#        print (city['airport'],city['pinyin'])
cn_airports = [ city for city in citis if city['pinyin'] != '']    #将国外机场信息过滤掉 国外的“pinyin==‘’”
with open('cn_airports.csv','w') as f:
    #f.write('No' + ',' + 'airport' + ',' + 'city' + ',' + 'enAirport' + ',' + 'match' + ',' + 'pinyin' + ',' + 'tcode' + '\n')
    #f.write('airport' + ',' + 'city' + ',' + 'enAirport' + ',' + 'match' + ',' + 'pinyin' + ',' + 'tcode' + '\n')
    No = 0
    for i in cn_airports:
        f.write(str(No)+',')
        for value in i.values():
            f.write(value +',')

        f.write('\n')
        No += 1

print(len(cn_airports))
from bs4 import BeautifulSoup  # 用于爬取的网页文字处理
# import re         #🈷️用于正则
import requests  # urllib3的应用
# import json
import datetime
import time


def getdates(date_info, n=0):
    if date_info != '':
        date_info_c = datetime.datetime.strptime(date_info, '%Y-%m-%d')  # strftime('%Y-%m-%d')   #日期string类型转为'日期型'
    else:
        date_info_c = datetime.date.today()
    # print(type(date_info_c))
    # d = datetime.datetime.strptime(detester,’%Y-%m-%d')
    # print (date_info_c)

    # 未来n天的时间取得
    days_cal = []
    for day in range(0, int(n+1)):
        date_in = date_info_c + datetime.timedelta(days=day)
        date_in_str = date_in.strftime('%Y-%m-%d')  # 日期型转化string并格式[YYYY-MM-DD]转换
        days_cal.append(date_in_str)
    print(days_cal)
    return days_cal


def spider_pro(dep_city, arr_city, date_info, ndays=0):

    #date_infos = getdates(date_info=date_info, n=ndays)

    #with open('airline_info.csv','a') as f:
        #for date_info in date_infos:

    #########爬取网页数据  Start################
    url = 'http://www.umetrip.com/mskyweb/fs/fa.do?dep={0}&arr={1}&date={2}&channel='.format(dep_city, arr_city,
                                                                                         date_info)
    # url = 'http://www.umetrip.com/mskyweb/fs/fa.do?dep=DLC&arr=PEK&date=2018-10-03&channel='
    req = requests.get(url)
    #req.encoding = 'utf-8'
    # soup = BeautifulSoup(req.text,'html.parser',from_encoding= "utf-8")  #获取网页源码  html.parser在此处不灵
    # soup = BeautifulSoup(req.text,'lxml',from_encoding= "utf-8")  #获取网页源码  lxml在此处不灵
    soup = BeautifulSoup(req.text, 'xml', from_encoding="utf-8")  # 获取网页源码
    temps = soup.find_all('div', 'li_com')  ##查询div标签下的class='li_com'的所有内容 返回list类型
    print(len(temps))
    return temps
    #########爬取网页数据  End################

def data_pro(temp,date_info):
    temp_list = temp.text.replace('+', '').replace('\"', '').replace('\n', '').split('	')  # 取得所用的文字信息,去掉+,\",\n,TAB
    a = [i for i in temp_list if i != '' and i != '  ']  # 过滤掉空元素及无效元素
    new_a = []
    # print("".join(a[2].split()))
    a[2] = a[2].lstrip().rstrip().split()
    a[3] = a[3].lstrip().rstrip().split('/')
    a[4] = a[4].lstrip().rstrip().split()
    a[-1] = date_info  # 将就后列信息改为 日期信息
    for j in range(0, 2):
        new_a.append(a[j])

    for k in range(2, 5):
        new_a.extend(a[k])

    new_a.append(a[-1])
    #for info in new_a:
    #    f.write(info+',')
    #f.write('\n')
    print(new_a)
    return  new_a


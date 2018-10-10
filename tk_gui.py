# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
import spider
import datetime,time
import tkinter
import pandas as pds
import numpy as np

def spider_s():
    today = str(datetime.date.today())
    dep_city = dep_city_e.get()
    #dep_city ='DLC'
    ndays = int(dep_day.get())

    disp_info.config(state=NORMAL)
    disp_info.insert(END, '爬取 《航旅纵横》机场航班信息\n')
    disp_info.insert(END, '<<<<Start>>>>\n')
    disp_info.insert(END, 'In processing...\n')
    base_w.update()
    disp_info.config(state=DISABLED)

    if chVarUn.get():
        print ('Yes')
        names = ['No','airport','city','enAirport','match','pinyin','tcode']
        airports = pds.read_csv('cn_airports.csv',names=names,index_col=False)
        arr_citys = np.array(airports['tcode']).tolist()
        disp_info.config(state=NORMAL)
        num = 1
        for arr_city in arr_citys:
            ok = spider.spider_pro(dep_city=dep_city, arr_city=arr_city, date_info=today, ndays=ndays)

            if ok == 'ok':
                disp_info.insert(END, 'No.{0}:AirLine_info from {1} to {2} has got!\n'.format(num,dep_city,arr_city))
                num += 1
            else:
                disp_info.insert(END, 'Waiting...\n')

            base_w.update()
        disp_info.insert(END,'{0} informations had collected!!! '.format(num))
        disp_info.config(state=DISABLED)

    else:
        arr_city = arr_city_e.get()
        #print(ndays)
        #print(dep_city,arr_city)
        #d1 = len(dep_city)
        #a1 = len(arr_city)
        ok = spider.spider_pro(dep_city = dep_city,arr_city=arr_city,date_info = today,ndays = ndays)      #调用爬取处理function
        disp_info.config(state=NORMAL)
        if ok == 'ok':

            disp_info.insert(END, '<<<<End>>>>\n')

        else:
            disp_info.insert(END, 'Waiting...\n')
        disp_info.config(state=DISABLED)

    return

base_w = Tk()
base_w.title('<GUI>爬虫小程序')
base_w.geometry('680x500+450+100')  # 调整窗口及屏幕位置

dep_city_l= Label(base_w, text='起飞机场：',backgroup = None)
dep_city_l.grid(row=0, column=0, sticky=W)

dep_city_e = Entry(base_w)
dep_city_e.grid(row=0, column=1, sticky=E)

dep_day_l1 =Label(base_w,text ='未来',width =5)
dep_day_l1.grid(row =0, column =2 ,stick =E)


dep_day = Spinbox(base_w, from_ = 0 ,to =10,increment =1,width =3 )
dep_day.grid(row =0, column =3 ,columnspan =2,stick =W)
dep_day_l2 =Label(base_w,text ='天',width =5)
dep_day_l2.grid(row =0, column =3 ,stick =E)

arr_city_l= Label(base_w, text='目的机场：')
arr_city_l.grid(row=1, column=0, sticky=W)
arr_city_e = Entry(base_w)
arr_city_e.grid(row=1, column=1, sticky=E)

chVarUn = tkinter.IntVar()
ck_box =tkinter.Checkbutton(base_w,text='起飞机场的所有航班',variable =chVarUn)
#ck_box =tkinter.Checkbutton(base_w,text='起飞机场的所有航班')
ck_box.deselect()
ck_box.grid(row = 1,column = 2,sticky = E)

#but = Button(base_w,text= '开始',command =spider_s)
but = Button(base_w,text= '开     始',command =spider_s)
but.grid(row=1,column = 3,sticky =E)
but = Button(base_w,text= '保存到文件')
but.grid(row=1,column = 4,sticky =W)

disp_info = Text(base_w,width = 95)
disp_info.config(state = DISABLED)
disp_info.grid(row = 3 ,column =0,columnspan = 5,sticky = W)

bu_cl = Button(base_w,text= '中止',command =but.quit)
bu_cl.grid(row=4,column = 0,columnspan = 5,sticky =E)

base_w.mainloop()

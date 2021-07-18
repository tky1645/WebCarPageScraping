# nishioka CopyRight
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
import Class as cl
import WebMethod

#ブラウザをインスタンス化
browser = WebMethod.Browser_Init()

names_Goo = cl.NamesGoo()

#ページアクセス
browser.get(names_Goo.url_Top)
element_form= browser.find_element_by_id(names_Goo.idname_input)
#キーワード検索
element_form.send_keys(names_Goo.keyword)
browser.find_element_by_id(names_Goo.idname_serchBtn).click()

#要素の取得
title=[]
distance = []
year = []
total_price = []

while True:

    list = browser.find_elements_by_class_name('textBox')
    for l in list:
        price_area=l.find_element_by_css_selector('.clumn_left.clearfix')
        #タイトル
        elem_title = l.find_element_by_class_name('car_name').text
        #年式
        detail_middle =  price_area.find_element_by_class_name('clumn_left_middle')
        elem_year = detail_middle.find_element_by_tag_name('p').text
        #走行距離
        detail_bottom = price_area.find_element_by_class_name('clumn_left_bottom')
        elem_distance = detail_bottom.find_elements_by_tag_name('p')[1].text


        elem_price=l.find_element_by_class_name('totalPrice').text

        title.append(elem_title)
        year.append(elem_year)
        distance.append(elem_distance)
        total_price.append(elem_price)


    #ページ遷移
    try:
        elem_nextBtn = browser.find_element_by_class_name('next')
        elem_nextBtn.click()
    except:
        break

df = pd.DataFrame()
df['title'] = title
df['total_price'] = total_price
df['distanece'] = distance
df['year'] = year





df.to_csv('Output.csv',encoding='utf_8_sig')



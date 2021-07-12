# nishioka CopyRight
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
import Class as cl
import WebMethod

#ブラウザをインスタンス化
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver.exe',options=options)

names_Goo = cl.NamesGoo()

#ページアクセス
browser.get(names_Goo.url_Top)
element_form= browser.find_element_by_id(names_Goo.idname_input)
#キーワード検索
element_form.send_keys(names_Goo.keyword)
browser.find_element_by_id(names_Goo.idname_serchBtn).click()

#test
list = browser.find_elements_by_class_name('CarName')
for l in list:
    print(l.text)

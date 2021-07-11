from selenium import webdriver
import selenium
import pandas as pd

def Get_elementText_byId(browser, idName):
    #要素が見つからないときは5s待つ
    browser.implicitly_wait(5) 
    #要素が存在しない
    #複数要素存在するの場合はエラーを返す
    print(browser.current_url)
    print(idname)
    elem = browser.find_element_by_class_name('gNO89b')
    print(elem)
    print(elem.text)
    text = elem.text
    return text

browser = webdriver.Chrome('chromedriver.exe')
#url = 'https://www.carsensor.net/usedcar/index.html?STID=CS210610&AR=35*33*30*32*31&BRDC=&CARC=TO_S219&NINTEI=&CSHOSHO='
url = 'https://www.google.com/'
browser.get(url)

idname = 'lnXdpd'
temp = Get_elementText_byId(browser, idname)
print(temp)





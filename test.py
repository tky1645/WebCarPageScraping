from selenium import webdriver
import selenium
import pandas as pd

#web要素1つだけ取得する
def Get_elementText_byId(browser, idName):
    browser.implicitly_wait(5) 
    #ガード｜唯一の要素でない場合はエラーを返す
    temp = browser.find_elements_by_class_name(idname)
    if len(temp) is not 1:
        return None
    try:
        elem = browser.find_element_by_class_name(idname)
    #要素が存在しない
    except NoSuchElementException as e:
        return None
    except:
        return None

    return elem.text

#test
browser = webdriver.Chrome('chromedriver.exe')
url = 'https://www.google.com/'
url = 'https://www.goobike.com/maker-honda/car-dj_1r/index.html'
browser.get(url)

idname = 'lnXdpd'
idname = 'bike_sec'
temp = Get_elementText_byId(browser, idname)
print('戻り:'+temp)





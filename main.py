# nishioka CopyRight
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver.exe',options=options)

url= 'https://www.carsensor.net/'
browser.get(url)
element_form= browser.find_element_by_id('js-fw-input')

key_word='NSX'
element_form.send_keys(key_word)
browser.find_element_by_class_name('freewordWrap__submit').click()

#要素が見つからないときは5s待つ
browser.implicitly_wait(5) 
class_name_caset = 'caset js_listTableCassette'
class_name_bodyTitle = 'casetMedia__body__title'
class_name_basePrice = 'basePrice__price__main'
class_name_totalPrice = 'totalPrice__price__main'

title = []
base_price = []
total_price = []
while True:
    #element_caset = browser.find_element_by_class_name('caset js_listTableCassette') # 取得できない
    #element_caset = browser.find_element_by_id('VU6242860653_cas')# idなら取得できる
    element_caset = browser.find_elements_by_css_selector('.caset.js_listTableCassette') # 取得できた

    for elem in element_caset:
            element_title = elem.find_element_by_class_name(class_name_bodyTitle).text
            #価格がない場合は０で代用
            try:
                element_basePrice = elem.find_element_by_class_name(class_name_basePrice).text
                element_totalPrice = elem.find_element_by_class_name(class_name_totalPrice).text
            except:
                element_basePrice = 0
                element_totalPrice = 0
    
            title.append(element_title)
            base_price.append(int(element_basePrice))
            total_price.append(int(element_totalPrice))

    #ページ内のデータを整形
    df = pd.DataFrame()
    df['title'] = title
    df['basePrice'] = base_price
    df['totalPrice'] = total_price

    # ページ遷移
    elem_nextBtn = browser.find_element_by_xpath('//*[@id="js-resultBar"]/div[2]/div/div[2]/button[2]')
    if elem_nextBtn.is_enabled(): 
        elem_nextBtn.click()
    else:
        break

df.to_csv('test.csv',encoding='utf_8_sig')
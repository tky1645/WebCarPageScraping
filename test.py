from selenium import webdriver
import selenium
import pandas as pd

browser = webdriver.Chrome('chromedriver.exe')
#url = 'https://www.carsensor.net/usedcar/index.html?STID=CS210610&AR=35*33*30*32*31&BRDC=&CARC=TO_S219&NINTEI=&CSHOSHO='
url = 'https://www.carsensor.net/usedcar/bTO/s219/index{}.html?AR=35%2A33%2A30%2A32%2A31'.format(3)
browser.get(url)

elem_nextBtn = browser.find_element_by_xpath('//*[@id="js-resultBar"]/div[2]/div/div[2]/button[2]')
print(elem_nextBtn.is_enabled())


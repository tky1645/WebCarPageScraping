#WebMethod.py
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

#ブラウザをインスタンス化
def Browser_Init(Is_useOption=True):
    if Is_useOption: 
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome('carpageScrapingApp\BikeScrapingPackage\chromedriver.exe',options=options)
        #browser = webdriver.Chrome('chromedriver.exe',options=options)
        #browser = webdriver.Chrome(executable_path=r'C:\Users\takuya\Documents\Github\WebCarPageScraping\ScrapingProject\CarpageScrapingApp\BikeScrapingPackage\chromedriver.exe',options=options)
    else:
        #browser = webdriver.Chrome(executable_path=r'.\ScrapingProject\CarpageScrapingApp\BikeScrapingPackage\chromedriver.exe')
        browser = webdriver.Chrome('carpageScrapingApp\BikeScrapingPackage\chromedriver.exe')
    return browser



#web要素1つだけ取得する
def Get_elementText_byId(browser, idName):
    browser.implicitly_wait(5) 
    #ガード｜唯一の要素でない場合はエラーを返す
    temp = browser.find_elements_by_class_name(idName)
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


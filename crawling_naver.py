from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
kword = input('검색어를 입력하세요.:')
base_url = url + quote_plus(kword)
#base_url

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
'''
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(10)
driver.get(base_url)

body = driver.find_element_by_css_selector('body')

#페이지 다운시켜서 더 많은 이미지가 나오게 한다.
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

#find_elements(전체를 찾음)
imgs = driver.find_elements_by_css_selector('img._img')
n = 1
for idx, img in enumerate(imgs):
    #print(idx,img.get_attribute('src'))
    imgUrl =  img.get_attribute('src')
    imgName = './data/' + kword + str(idx) + '.jpg'
    urllib.request.urlretrieve(imgUrl,imgName)

driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://animego.org/anime/season/2023/spring")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
list_title = []
var_title = []
SCROLL_PAUSE_TIME = 0.5



def get_page():
    # получаем высоту страницы
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        #скролим вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # пауза
        time.sleep(SCROLL_PAUSE_TIME)
        # опять скролим по высоте,
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            main_page = driver.page_source
            soup = BeautifulSoup(main_page, 'html.parser')
            page = soup.prettify()
            fil = open("link/somefile.txt", "w")
            for i in soup.find_all("div", class_ = "h5 font-weight-normal mb-1"):
                list_title.append(f"{i}\n")
                #f.write(f"{i[:sort_by_href]}{i[sort_by_href:]}</a>\n")
            for i in list_title:
                var_title.append(i[40:-11])
            for i in var_title:
                fil.write(f"{i}</a>\n")
            fil.close()
            driver.close()
            return var_title
        last_height = new_height
        
            
        




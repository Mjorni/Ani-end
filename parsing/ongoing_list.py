import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs

ongoing_list = []


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
count_page = 1

def pars_page():
    page = f"https://animego.org/anime/status/ongoing?sort=a.createdAt&direction=desc&type=animes&page={count_page}"
    soup = requests.get(page, headers=headers)
    soup = bs(soup.text, 'html.parser')
    
    a = soup.find_all("div", class_ = 'h5 font-weight-normal mb-1')
    for i in a:
        ongoing_list.append(f"{i}")
    return ongoing_list


   
"""with open("/Users/poko/Documents/PythonProject/AniEnd/ani-end/link/ongoing_list.txt", "w") as f:
    for i in pars_page():
         f.write(i + "\n")
    pass"""



"""
    
if __name__ == "__main__":
    get_ongoing_list()
    """
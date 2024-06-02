import requests
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def requests_searching_anime(url):
    list_result = []
    "начало поиска и конце поиска"
    req_get = requests.get(url, headers=headers)
    start_seacrh = req_get.text.find('class="animes-grid position-relative"')
    end_search = req_get.text.find('class="footer-push"', start_seacrh)
    count_result_search = req_get.text.count('class="h5 font-weight-normal mb-2 card-title text-truncate"')
    "начало поиска тайтлов на странице"
    txt_for_found = 'class="h5 font-weight-normal mb-2 card-title text-truncate"'
    start_seacrh_element = req_get.text.find(txt_for_found) + len(txt_for_found) + 1
    end_search_element = req_get.text.find('</div>', start_seacrh_element)
    end_search_point = req_get.text.find('>', end_search_element)
    list_result.append(f"{req_get.text[start_seacrh_element: end_search_element]}")
    while len(list_result) != count_result_search:
        temp_var_start = req_get.text.find(txt_for_found, end_search_element) + len(txt_for_found) + 1
        temp_var_end = req_get.text.find('</div>', temp_var_start)
        end_search_element = temp_var_start
        list_result.append(f"{req_get.text[temp_var_start: temp_var_end]}")
    
    with open("./link/page.txt", "w") as f:
        for i in list_result:
            f.write(f"{i}\n")
    return list_result

if __name__ == "__main__":
    requests_searching_anime()
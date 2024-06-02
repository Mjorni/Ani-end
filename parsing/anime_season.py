import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
main_page_url = requests.get("https://animego.org", headers=headers) # Сайт с аниме
get_http_season = requests.get("https://animego.org/anime/season/2023/spring", headers=headers)
class anime_seas():
    def get_name_title():
        start = get_http_season.text.find('<div class="h5 font-weight-normal mb-1">') + 40  #начало поиска
        end = get_http_season.text.find('</a></div><div class="text-gray-dark-6 small mb-2">') #начало поиска
        count_title_on_season = get_http_season.text.count('<div class="col-12" data-page="1">') #количество тайтлов
        list_title = []
        list_title.append(get_http_season.text[start:end]) #Первое добавление
        while len(list_title) != count_title_on_season:
            """цикл, который каждый раз меняет переменные для поиска от и до"""
            temp_var_start = get_http_season.text.find('<div class="h5 font-weight-normal mb-1">', end) + 40 #20030
            temp_var_end = get_http_season.text.find('</a></div><div class="text-gray-dark-6 small mb-2">', temp_var_start)
            end = temp_var_start
            #print(f"начало: {temp_var_start}, \nКонец{temp_var_end}")
            list_title.append(get_http_season.text[temp_var_start:temp_var_end])
        """Запись в файл"""
        f_s = open(".\link\with_link.txt", "w")
        for i in list_title:
            sort_by_href = i.find(">") + 1
            f_s.write(f"{i[:sort_by_href]}{i[sort_by_href:]}</a>\n")
        f_s.close()
        return list
    
    
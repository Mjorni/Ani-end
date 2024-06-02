import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
main_page_url = requests.get("https://animego.org", headers=headers) # Сайт с аниме

class last_titles:
    def get_day():
        f = open(".\link\last_title.txt", "w")
        """Запист даты"""
        start = main_page_url.text.find('<div class="h6 d-flex mr-auto mb-0" data-label="') + 47
        end = main_page_url.text.find('>', start)
        day = main_page_url.text[start:end]
        f.write(f"{day}\n")
        f.close()
        return day[1:-1]


    def get_anime():
            """Аниме дня"""
            "Начало поиска"  
            str_for_search = '<div class="d-flex align-items-center">'
            start = main_page_url.text.find(str_for_search) + len(str_for_search)
            title_list = []
            "Конец поиска"
            end_search_point = main_page_url.text.find('class="card-header last-update-header d-flex align-items-center"', start)
            #end_search_point = main_page_url.text.find('<span class="mr-1">Вчера</span>')
            
            "Поиск названий аниме"
            str_for_search_title = '<span class="last-update-title font-weight-600">'
            len_str = len(str_for_search_title)
            start_search_title_name = main_page_url.text.find(str_for_search_title, start, end_search_point) + len_str
            end_search_title_name = main_page_url.text.find('</span>', start, end_search_point)
            count_title_anime = main_page_url.text.count('<span class="last-update-title font-weight-600">',start, end_search_point)
            
            name_title_series = main_page_url.text[start_search_title_name:end_search_title_name]
            

            "Поиск серии"
            str_for_search_number = '<div class="ml-3 text-right"><div class="font-weight-600 text-truncate">'
            len_str_for_number = len(str_for_search_number)
            str_for_end_search_number = '</div><div class="text-gray-dark-6">'

            start_search_number = main_page_url.text.find(str_for_search_number, start, end_search_point) + len_str_for_number
            end_search_number = main_page_url.text.find(str_for_end_search_number, start, end_search_point)
            count_title_number = main_page_url.text.count(str_for_search_number, start, end_search_point)
            
            number_title_series = main_page_url.text[start_search_number:end_search_number]

            "Поиск озвучки"
            str_for_search_sound = '</div><div class="text-gray-dark-6">'
            len_str_for_sound = len(str_for_search_sound)
            str_for_search_end_sound = '</div></div>'

            start_search_sound = main_page_url.text.find(str_for_search_sound, start, end_search_point) + len_str_for_sound
            end_search_sound = main_page_url.text.find(str_for_search_end_sound, start, end_search_point)

            sound_title_series = main_page_url.text[start_search_sound:end_search_sound]


            "Ссылка на страницу"
            str_for_search_link = '<div class="last-update-item list-group-item list-group-item-action border-left-0 border-right-0 border-bottom-0'
            count_link = main_page_url.text.count(str_for_search_link, 0, end_search_point)
            str_end_search_link = 'tabindex="-1">'
            str_for_href = 'href='
            link_sort = len(str_for_href) + 1
            
            for_search_link = main_page_url.text.find(str_for_search_link)

            index_start = main_page_url.text.find(str_for_href, for_search_link) + link_sort
            index_end = main_page_url.text.find(str_end_search_link) - 3
            index_html = main_page_url.text.find(str_for_href, index_start) + link_sort
        
            href_title_series = main_page_url.text[index_start:index_end]
            

            title_list.append(f'<a href="https://animego.org{href_title_series}">{name_title_series}</a> | {number_title_series} {sound_title_series}\n')

            while len(title_list) != count_title_anime:
                "Для ссылки"
                temp_var_for_link_start = main_page_url.text.find(str_for_href, index_start) + link_sort
                temp_var_for_link_end = main_page_url.text.find(str_end_search_link, temp_var_for_link_start) - 3
                index_start = temp_var_for_link_start

                "для названия"
                temp_var_for_name_start = main_page_url.text.find(str_for_search_title, end_search_title_name) + len_str
                temp_var_for_name_end = main_page_url.text.find('</span>', temp_var_for_name_start)
                end_search_title_name = temp_var_for_name_start

                "Для серии"
                temp_var_for_number_start = main_page_url.text.find(str_for_search_number, end_search_number) + len_str_for_number
                temp_var_for_number_end = main_page_url.text.find(str_for_end_search_number, temp_var_for_number_start)
                end_search_number = temp_var_for_number_start

                "Для озвучки"
                temp_var_for_sound_start = main_page_url.text.find(str_for_search_sound, end_search_sound) + len_str_for_sound
                temp_var_for_sound_end = main_page_url.text.find(str_for_search_end_sound, temp_var_for_sound_start)
                end_search_sound = temp_var_for_sound_start


                temp_name = main_page_url.text[temp_var_for_name_start:temp_var_for_name_end]
                temp_number = main_page_url.text[temp_var_for_number_start:temp_var_for_number_end]
                temp_sound = main_page_url.text[temp_var_for_sound_start:temp_var_for_sound_end]
                temp_link = main_page_url.text[temp_var_for_link_start:temp_var_for_link_end]
                title_list.append(f'<a href="https://animego.org{temp_link}">{temp_name}</a> | {temp_number} {temp_sound}\n')
            

            f = open(".\link\last_title.txt", "w")
            for i in title_list:
                f.write(i)
            f.close()

if __name__ == "__main__":
     last_titles.get_anime()
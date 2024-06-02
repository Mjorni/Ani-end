import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
main_page_url = requests.get("https://animego.org", headers=headers) # Сайт с аниме


class random_title():
    def random_anime():
        """Cлучайное аниме"""
        url = requests.get('https://animego.org/anime/random')
        soup = bs(url.text, 'html.parser')
        a = soup.find("div", id ='escription pb-3')
        name_title = url.text.find("<title>") + len("<title>")
        link_title = url.text.find("link href=") + len("link href=")
        end_link = url.text.find('rel="canonical"')
        print(a)
        #w.write(f'<a href="{url.text[name_title:url.text.find("смотреть онлайн")]}')
        "Для подсчёта серий"
        if 'Эпизоды</dt><dd class="col-6 col-sm-8 mb-1">' in url.text:
            html_for_start_count_episode = url.text.find('Эпизоды</dt><dd class="col-6 col-sm-8 mb-1">') + len('Эпизоды</dt><dd class="col-6 col-sm-8 mb-1">')
            html_for_end_count_episode = url.text.find('<', html_for_start_count_episode)
            get_count_epidose = url.text[html_for_start_count_episode:html_for_end_count_episode]
            "Для подсчёта оценки"
            get_star_start = url.text.find('<span class="rating-value">') + len('<span class="rating-value">')
            get_star_end = url.text.find('</span>', get_star_start)
            get_star = url.text[get_star_start:get_star_end]
            return f'''
        <a href={url.text[link_title:end_link]}>{url.text[name_title:url.text.find("смотреть онлайн")]}</a>\n
        Количество серий:\t{get_count_epidose}\nоценка\t"{get_star}"
        '''
        else:
            html_for_start_manga = url.text.find('Первоисточник') + len('Первоисточник')
            html_for_end_manga = url.text.find("/dd", url.text.find('</dt><dd class="col-6 col-sm-8 mb-1">', html_for_start_manga))
            get_count_epidose = url.text[html_for_start_manga:html_for_end_manga]
            str_for_filtr = url.text.find('</dt><dd class="col-6 col-sm-8 mb-1">', html_for_start_manga) + len('</dt><dd class="col-6 col-sm-8 mb-1">')
            lf_symbol = url.text.find('<', str_for_filtr)
            endresult = url.text[str_for_filtr:lf_symbol]
            "Для подсчёта оценки"
            get_star_start = url.text.find('<span class="rating-value">') + len('<span class="rating-value">')
            get_star_end = url.text.find('</span>', get_star_start)
            get_star = url.text[get_star_start:get_star_end]
            return f'''<a href={url.text[link_title:end_link]}>{url.text[name_title:url.text.find("смотреть онлайн")]}</a>\nПервоисточник:\t{endresult}\nоценка\t"{get_star}"'''
        
        

if __name__ == "__main__":
    random_title.random_anime()
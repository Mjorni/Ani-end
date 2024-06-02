import requests
import logging
import asyncio #импорт асинхронного модуля

from aiogram import Bot, Dispatcher, types
from aiogram.utils.deep_linking import decode_payload
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
#pip install -U --pre aiogram необходимо установить
from parsing.anime_season import anime_seas
from parsing.last_anime import last_titles
from parsing.random_anime import random_title
from parsing.search_title import requests_searching_anime
from states import list_states



logging.basicConfig(level=logging.INFO)

api_link = "https://api.telegram.org/bot5620854110:AAFtbKtXRcoUQDur6TYVGm3XE5t56xCyg4g" #апи бота
bot = Bot(token="5620854110:AAGjAMj7-NZkg04x2PYPTqlzDfHuICsidnU", parse_mode=types.ParseMode.HTML)
admin_token = 892957916 #id админа(я)
#346038776 id лизы для проверки

loop = asyncio.get_event_loop() #не помню
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage()) #диспатчер 



@dp.message_handler(lambda message: message.text == "start")
async def cmd_start(message: types.Message):
    """Запуск бота"""
    key_button =[
                   [types.KeyboardButton(text='Случайное аниме')],
                   [types.KeyboardButton(text='Аниме Сезона')],
                   [types.KeyboardButton(text='Последнее аниме')],
                   [types.KeyboardButton(text='Поиск')]
                   #[types.KeyboardButton(text='Подписки')]
                ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=key_button,
        resize_keyboard=True, #меняем размер кнопок
        input_field_placeholder="Выберите что отправить" #Задний текст в поле ввода
        )
    await message.answer("Что вы хотите найти?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text =='img')
async def cmd_img(message: types.Message):

    if message.text.lower() == 'img': #Если пользователь ввел: img - то бот скидывает картинку по ссылке
        await bot.send_photo(chat_id=message.from_user.id, photo='https://sun9-15.userapi.com/1H233EQaOutctwUmfL8mb3aZQPCyIlhBt2_6YA/BceXIbPV78o.jpg')
        
    elif message.text.lower() == 'audio':
        await bot.send_audio(chat_id=message.from_user.id, audio='D:\Download\chacha.mp3')
    else:
        pass
        #отвечает пользователю копией его сообщения
        """text = f"{message.text}"
        await bot.send_message(chat_id=message.from_user.id, text=text)
        """

@dp.message_handler(lambda message: message.text == "Аниме Сезона")
async def anime_season(message: types.Message):
    #anime_seas.get_name_title()
    """Аниме сезона и ссылки на тайтлы""" 
    #with open(".\link\with_link.txt", "r") as f:
    #await message.answer(f"Сейчас выходит:\n\n{f.read()}")
    
        #await message.answer(f"Анмие сезона\n\n{f.read()}")
    with open("link/somefile.txt", "r") as fil:
            await message.answer(fil.read())
    

@dp.message_handler(lambda message: message.text == "Последнее аниме")
async def last_anime(message: types.Message):
    last_titles.get_anime()
    """Последнее аниме на сайте"""  
    f = open(".\link\last_title.txt", "r")
    await message.answer(f"Вот что сегодня вышло:\n{f.read()}")
    f.close()

@dp.message_handler(lambda message: message.text =='Случайное аниме')
async def cmd_random(message: types.Message):
    await message.answer(f"{random_title.random_anime()}")
    #await requests_searching_anime()


"Алгоритм поиска аниме"
@dp.message_handler(lambda message: message.text =='Поиск')
async def get_state(message: types.Message):
    await message.answer("Что вы хотите найти?")
    await list_states.name_anime.set()

@dp.message_handler(state=list_states.name_anime)
async def search(message: types.Message, state: FSMContext):
    requested_anime = message.text.lower().replace(" ", "+")
    url = (f"https://animego.org/search/anime?q={requested_anime}")
    requests_searching_anime(url)
    with open("link/page.txt", "r") as f:
        await message.answer(f.read())
    await state.update_data(name_anime = f"{url}{requested_anime}")
    await state.finish()
    
   
"алгоритм подписки на  аниме" 
@dp.message_handler(lambda message: message.text == "Подписки")
async def follow(message: types.Message):
    await message.answer("На какое аниме вы хотите подписаться?")
    with open("link/ongoing_list.txt", "w") as f:
        pass
    await list_states.follow_anime.set()
    
    
@dp.message_handler(state=list_states.follow_anime)
async def follow_anime(message: types.Message, state: FSMContext):
    test_for_user = message.text.lower().replace(" ", "+")
    url = (f"https://animego.org/search/anime?q={test_for_user}")
    print(url)
    
 
from aiogram import executor, types
from Conf import bot, admin_token, dp
from parsing.anime_on_season import get_page

if __name__ == "__main__":
    get_page()
    async def send_to_admin(dp): # При запуске бота будет написанно "бот запущен"
        key_button =[
                   [types.KeyboardButton(text='start')]
                ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=key_button,
            resize_keyboard=True, #меняем размер кнопок
            input_field_placeholder="Нажмите кнопку start"
        )
        await bot.send_message(chat_id=admin_token, text="""
        Охаё, Для начала необходимо запустить бота
        что делают команды бота:
    Случайное аниме - выдаёт случайно аниме с сайта
    Аниме сезона - выдаёт список аниме которые сейчас выходят
    Последнее аниме - список аниме которые вышли сегодня""", 
            reply_markup = keyboard)
        
        


executor.start_polling(dp, on_startup=send_to_admin)  
from aiogram.dispatcher.filters.state import StatesGroup, State

class list_states(StatesGroup):
    name_anime = State()
    follow_anime = State()
    

    
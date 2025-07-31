from aiogram.fsm.state import State, StatesGroup

class OrderForm(StatesGroup):
    waiting_for_order = State()

class LanguageForm(StatesGroup):
    waiting_for_language = State()

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards import get_language_menu, get_main_menu
from states import LanguageForm

router = Router()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer(
        "Пожалуйста, выберите язык / Please select a language:",
        reply_markup=get_language_menu()
    )
    await state.set_state(LanguageForm.waiting_for_language)

@router.callback_query(lambda c: c.data in ["lang_ru", "lang_en"])
async def select_language(callback: CallbackQuery, state: FSMContext):
    language = "ru" if callback.data == "lang_ru" else "en"
    await state.update_data(language=language)
    
    if language == "ru":
        await callback.message.edit_text(
            "Приветствую!\n\nЭто бот-портфолио и бот для связи со мной.\nВыбери интересующий раздел:",
            reply_markup=get_main_menu(language)
        )
    else:
        await callback.message.edit_text(
            "Welcome!\n\nThis is a portfolio bot and a bot to contact me.\nChoose the section you are interested in:",
            reply_markup=get_main_menu(language)
        )
    
    await state.set_state(None)
    await callback.answer()

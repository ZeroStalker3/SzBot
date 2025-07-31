from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards import get_main_menu, get_back_button
from database import get_user_orders
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from github_integration import get_github_activity


router = Router()

@router.callback_query(lambda c: c.data == "info")
async def show_info(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = (
            "👨‍💻 Я разрабатываю свои проекты на C# и Python.\n\n"
            "📚 Мои основные навыки:\n"
            "- Разработка веб-приложений на Django и Flask, Web-App (C#)\n"
            "- Создание ботов для Telegram с использованием aiogram\n"
            "- Работа с базами данных (PostgreSQL, SQLite, MsSQL)\n"
            "- Опыт работы с Git и GitHub\n"
            "- Разработка десктопных приложений на C# и Python (простые)\n\n"
            "🔧 Инструменты и технологии, которые я использую:\n"
            "- Visual Studio Code, Visual Studio 2022\n"
            "- Docker (В процессе изучения)\n"
            "- CI/CD (GitHub Actions)\n\n"
        )
    else:
        text = (
            "👨‍💻 I develop my projects in C# and Python.\n\n"
            "📚 My main skills:\n"
            "- Web application development with Django and Flask, Web-App (C#)\n"
            "- Creating Telegram bots using aiogram\n"
            "- Working with databases (PostgreSQL, SQLite, MsSQL)\n"
            "- Experience with Git and GitHub\n"
            "- Development of desktop applications in C# and Python (simple)\n\n"
            "🔧 Tools and technologies I use:\n"
            "- Visual Studio Code, Visual Studio 2022\n"
            "- Docker (Under study)\n"
            "- CI/CD (GitHub Actions)\n\n"
        )
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()

@router.callback_query(lambda c: c.data == "projects")
async def show_projects(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "💻 Примеры работ: [GitHub](https://github.com/ZeroStalker3)."
    else:
        text = "💻 Project examples: [GitHub](https://github.com/ZeroStalker3)."
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()

@router.callback_query(lambda c: c.data == "contacts")
async def show_contacts(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "📞 Связаться со мной: \n\nTelegram: @Shad_Zero \nEmail: (временно не доступно)"
    else:
        text = "📞 Contact me: Telegram: \n\n@Shad_Zero \nEmail: (temporarily unavailable)"
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()

@router.callback_query(lambda c: c.data == "resume")
async def show_resume(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "📄 Мое резюме: [Скачать PDF](Появится чуть позже)."
    else:
        text = "📄 My resume: [Download PDF](Coming soon)."
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()

@router.callback_query(lambda c: c.data == "reviews")
async def show_reviews(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "⭐ Пока отзывов нет, но скоро появятся!"
    else:
        text = "⭐ No reviews yet, but they will appear soon!"
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()

@router.callback_query(lambda c: c.data == "back")
async def go_back(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "Добро пожаловать обратно! \n\nЭто бот-портфолио и бот для связи со мной.\nВыбери интересующий раздел:"
    else:
        text = "Welcome back! \n\nThis is a portfolio bot and a bot to contact me.\nChoose the section you are interested in:"
    
    await callback.message.edit_text(text, reply_markup=get_main_menu(language))
    await callback.answer()


# Тествовые обработчики кнопок с выводом нужной информации, на данный моент я пока не добавляю в основом режиме
@router.callback_query(lambda c: c.data == "github_activity")
async def show_github_activity(callback: CallbackQuery, state: FSMContext):
    activity = get_github_activity()
    
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "Моя активность на GitHub:\n\n"
    else:
        text = "My GitHub activity:\n\n"
    
    for repo in activity:
        text += f"📁 {repo['name']}\n"
        text += f"📝 {repo['description']}\n"
        text += f"⭐ {repo['stars']}\n"
        text += f"🕒 Последнее обновление: {repo['last_updated']}\n\n"
    
    await callback.message.edit_text(text, reply_markup=get_back_button(language))
    await callback.answer()
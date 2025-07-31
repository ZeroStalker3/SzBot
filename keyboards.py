from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_language_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="English", callback_data="lang_en")]
        ]
    )

def get_main_menu(language="ru"):
    if language == "ru":
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="ℹ️ Информация обо мне", callback_data="info")],
                [InlineKeyboardButton(text="💻 Примеры работ", callback_data="projects")],
                #[InlineKeyboardButton(text="💻 Работы с GitHub", callback_data="github_activity")],
                [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
                #[InlineKeyboardButton(text="📄 Резюме (В разработке)", callback_data="resume")],
                [InlineKeyboardButton(text="⭐ Отзывы клиентов", callback_data="reviews")],
                [InlineKeyboardButton(text="📝 Форма заказа", callback_data="order")],
                #[InlineKeyboardButton(text="💼 Мои заказы", callback_data="my_orders")]
            ]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="ℹ️ About Me", callback_data="info")],
                [InlineKeyboardButton(text="💻 Projects", callback_data="projects")],
                #[InlineKeyboardButton(text="💻Project GitHub", callback_data="github_activity")],
                [InlineKeyboardButton(text="📞 Contacts", callback_data="contacts")],
                #[InlineKeyboardButton(text="📄 Resume (In Development)", callback_data="resume")],
                [InlineKeyboardButton(text="⭐ Client Reviews", callback_data="reviews")],
                [InlineKeyboardButton(text="📝 Order Form", callback_data="order")],
                #[InlineKeyboardButton(text="💼 My Orders", callback_data="my_orders")]
            ]
        )

def get_back_button(language="ru"):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🔙 Назад" if language == "ru" else "🔙 Back", callback_data="back")]]
    )

from aiogram import Router, F, Bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from states import OrderForm
from config import ADMIN_ID
from keyboards import get_main_menu
from database import get_user_orders, save_order
from aiogram.filters import Command
from utils import format_order
from utils import is_admin
from database import get_all_active_orders, save_order, mark_order_completed

router = Router()

class OrderForm(StatesGroup):
    waiting_for_order = State()

def get_cancel_button(language="ru"):
    if language == "ru":
        text = "❌ Отмена"
    else:
        text = "❌ Cancel"
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=text, callback_data="cancel_order")]]
    )

@router.message(Command("orders"))
async def list_orders(message: Message, state: FSMContext):
    await list_orders_handler(message, state)

@router.callback_query(lambda c: c.data == "back_to_orders")
async def back_to_orders(callback: CallbackQuery, state: FSMContext):
    await list_orders_handler(callback.message, state)
    await callback.answer()

async def list_orders_handler(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ У вас нет доступа к этой команде.")
        return

    data = await state.get_data()
    language = data.get("language", "ru")

    orders = await get_all_active_orders()
    if not orders:
        if language == "ru":
            await message.answer("📭 Пока нет активных заказов.")
        else:
            await message.answer("📭 No active orders yet.")
        return
    
    for order in orders:
        order_id, username, order_text = order
        if language == "ru":
            text = f"📌 Заказ #{order_id}\n👤 @{username}\n💬 {order_text}"
        else:
            text = f"📌 Order #{order_id}\n👤 @{username}\n💬 {order_text}"
        await message.answer(text, reply_markup=get_order_action_buttons(order_id))

@router.callback_query(lambda c: c.data == "order")
async def start_order(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "📝 Опишите ваш заказ. Например: \"Нужен Telegram-бот для заказов.\" Или нажмите ❌ Отмена."
    else:
        text = "📝 Describe your order. For example: \"Need a Telegram bot for orders.\" Or press ❌ Cancel."
    
    await callback.message.edit_text(text, reply_markup=get_cancel_button(language))
    await state.set_state(OrderForm.waiting_for_order)
    await callback.answer()

@router.message(OrderForm.waiting_for_order)
async def process_order(message: Message, state: FSMContext, bot: Bot):
    order_text = message.text
    await save_order(message.from_user.username, message.from_user.id, order_text)  # Сохранение в БД
    await state.clear()
    
    await bot.send_message(ADMIN_ID, f"📩 Новая заявка от @{message.from_user.username}:\n\n{order_text}")

    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "✅ Ваша заявка принята!"
    else:
        text = "✅ Your order has been accepted!"
    
    await message.answer(text, reply_markup=get_main_menu(language))

@router.callback_query(lambda c: c.data == "cancel_order")
async def cancel_order(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = "❌ Оформление заказа отменено. Если передумаете, можете попробовать снова."
        welcome_text = "Добро пожаловать обратно! \n\nЭто бот-портфолио и бот для связи со мной.\nВыбери интересующий раздел:"
    else:
        text = "❌ Order canceled. If you change your mind, you can try again."
        welcome_text = "Welcome back! \n\nThis is a portfolio bot and a bot to contact me.\nChoose the section you are interested in:"
    
    await callback.message.edit_text(text)
    await callback.message.answer(welcome_text, reply_markup=get_main_menu(language))
    await callback.answer()

def get_back_to_orders_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_orders")]]
    )

def get_order_action_buttons(order_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Выполнено", callback_data=f"complete_{order_id}")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_orders")]
        ]
    )

@router.callback_query(lambda c: c.data.startswith("complete_"))
async def complete_order(callback: CallbackQuery, state: FSMContext):
    order_id = int(callback.data.split("_")[1])
    await mark_order_completed(order_id)
    
    data = await state.get_data()
    language = data.get("language", "ru")
    
    if language == "ru":
        text = f"✅ Заказ #{order_id} отмечен как выполненный."
    else:
        text = f"✅ Order #{order_id} marked as completed."
    
    await callback.message.edit_text(text)
    await callback.answer()
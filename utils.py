import datetime

def get_current_time():
    """Возвращает текущее время в формате DD.MM.YYYY HH:MM."""
    return datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

def format_order(order):
    """Форматирует заказ для удобного отображения (из БД)."""
    order_id, username, user_id, order_text, created_at = order
    return (f"🆔 Заказ #{order_id}\n"
            f"👤 Пользователь: @{username} (ID: {user_id})\n"
            f"📅 Дата: {created_at}\n"
            f"📌 Текст заказа: {order_text}\n")

def is_admin(user_id):
    """Проверяет, является ли пользователь админом."""
    from config import ADMIN_ID
    return user_id == ADMIN_ID

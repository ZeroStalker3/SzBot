import sqlite3

DB_PATH = "orders.db"

def init_db():
    """Создание таблицы заказов, если её нет."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            user_id INTEGER,
            order_text TEXT,
            status TEXT DEFAULT 'active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

async def save_order(username, user_id, order_text):
    """Сохранение нового заказа."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (username, user_id, order_text, status) VALUES (?, ?, ?, 'active')",
        (username, user_id, order_text),
    )
    conn.commit()
    conn.close()

async def get_all_active_orders():
    """Получение всех активных заказов (не выполненных)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, order_text FROM orders WHERE status = 'active'")
    orders = cursor.fetchall()
    conn.close()
    return orders

async def mark_order_completed(order_id):
    """Пометка заказа как выполненного."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET status = 'completed' WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()

async def get_user_orders(user_id):
    """Получение заказов пользователя."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, order_text, status, created_at FROM orders WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    orders = cursor.fetchall()
    conn.close()
    return orders


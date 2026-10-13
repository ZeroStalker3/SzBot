# SzBot - Telegram Portfolio & Lead Generation Bot

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/aiogram-3.x-blue?logo=telegram" alt="aiogram">
  <img src="https://img.shields.io/badge/Database-SQLite/Postgres-lightgrey" alt="DB">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

## 📖 О проекте
**SzBot** — это телеграм-бот, выполняющий роль интерактивного портфолио и автоматизированной системы лидогенерации. Проект спроектирован с учетом масштабируемости, чистоты кода и лучших практик разработки асинхронных приложений. 

Бот позволяет потенциальным клиентам ознакомиться с моим стеком, кейсами и оставить структурированную заявку на разработку, которая автоматически доставляется и отслеживается.

## 🚀 Ключевые возможности
* **Интерактивное портфолио**: Навигация по навыкам, стеку и примерам работ через Inline-клавиатуры.
* **Lead Generation (Заказы)**: Многошаговая форма заказа (FSM) с валидацией данных и сохранением заявок в БД.
* **Админ-панель**: Управление лидами, смена статусов заказов, аналитика.
* **Асинхронная архитектура**: Неблокирующие операции ввода-вывода для высокой отказоустойчивости.

## 🛠 Стек технологий и Архитектура
* **Core**: Python 3.10+, `aiogram 3.x` (роутеры, FSM, Dispatcher).
* **Data Layer**: `SQLAlchemy` / `aiosqlite` (или другой ORM/драйвер, *уточнить по коду*), Repository Pattern.
* **Config**: `pydantic-settings` / `python-dotenv` (валидация переменных окружения).
* **Архитектурные паттерны**: Разделение на слои (Handlers -> Services -> Repositories), Dependency Injection (если применяется).

## ⚙️ Установка и запуск

### Требования
* Python 3.10+
* Docker & Docker Compose (опционально, для изолированного запуска)

### Шаг 1: Клонирование и окружение
```bash
git clone https://github.com/ZeroStalker3/SzBot.git
cd SzBot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Шаг 2: Конфигурация
Создайте файл `.env` в корне проекта на основе `.env.example`:

# Telegram
BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
ADMIN_ID=123456789

# Database
DATABASE_URL="sqlite+aiosqlite:///./szbot.db"

# App
LOG_LEVEL="INFO"

Шаг 3: Зависимости и миграции

```bash
pip install -r requirements.txt
# Инициализация БД / применение миграций (Alembic)
python -m src.database.init_db 
```

Шаг 4: Запуск

```bash
python -m bot
```

📁 Структура проекта (Refactored)
Рекомендуемая структура для масштабируемого бота:

SzBot/
├── bot/                  # Точка входа, конфигурация Dispatcher и роутеров
├── src/
│   ├── core/             # Конфиги (.env), логирование, DI
│   ├── database/         # Модели ORM, репозитории, сессии
│   ├── handlers/         # Обработчики команд и callback (разбиты по роутерам)
│   ├── keyboards/        # Генерация inline и reply клавиатур
│   ├── services/         # Бизнес-логика (например, OrderService)
│   └── states/           # Группы состояний FSM
├── .env                  # Переменные окружения (не коммитится!)
├── requirements.txt
└── README.md

### 📡 API бота (Команды и Callbacks)

# Пользовательские команды
| Команда | Описание |
|----------|--------|
|`/start`|Инициализация сессии, приветствие и главное меню|
|`/help`|Справка по функциональности бота|

# Административные команды
| Команда | Описание |
|----------|--------|
|`/orders`|Вывод пагинированного списка активных лидов (заявок)|

# FSM Сценарии

    Order Form: waiting_for_service ➔ waiting_for_budget ➔ waiting_for_description ➔ confirm_order.

# Контакты и Связь

    Telegram: @Shad_Zero
    GitHub: ZeroStalker3

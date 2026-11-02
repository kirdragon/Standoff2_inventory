import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загружаем настройки из .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Получаем строку подключения к PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Переменная DATABASE_URL не найдена в файле .env")

# Создаём движок SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

# Создаём фабрику сессий
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

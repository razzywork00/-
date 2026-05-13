import sqlite3
from config import DB_NAME


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        login TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        category_id INTEGER,
        status TEXT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        resource_id INTEGER,
        booking_date TEXT,
        start_time TEXT,
        end_time TEXT,
        status TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (resource_id) REFERENCES resources(id)
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM categories")
    categories_count = cursor.fetchone()[0]

    if categories_count == 0:
        categories = [
            ("Аудитории",),
            ("Ноутбуки",),
            ("Проекторы",),
            ("Компьютеры",),
            ("Конференц-залы",)
        ]

        cursor.executemany(
            "INSERT INTO categories (name) VALUES (?)",
            categories
        )

    cursor.execute("SELECT COUNT(*) FROM resources")
    resources_count = cursor.fetchone()[0]

    if resources_count == 0:
        resources = [
            ("Аудитория 101", "Учебный кабинет", 1, "Доступен"),
            ("Аудитория 202", "Компьютерный класс", 1, "Доступен"),
            ("Ноутбук Lenovo", "Ноутбук для занятий", 2, "Доступен"),
            ("Ноутбук HP", "Офисный ноутбук", 2, "Доступен"),
            ("Проектор Epson", "Мультимедийный проектор", 3, "Доступен"),
            ("Проектор Acer", "Проектор для презентаций", 3, "Доступен"),
            ("ПК Dell", "Компьютер для работы", 4, "Доступен"),
            ("ПК ASUS", "Игровой компьютер", 4, "Доступен"),
            ("Конференц-зал А", "Большой зал", 5, "Доступен"),
            ("Конференц-зал B", "Малый зал", 5, "Доступен")
        ]

        cursor.executemany("""
        INSERT INTO resources
        (name, description, category_id, status)
        VALUES (?, ?, ?, ?)
        """, resources)

    conn.commit()
    conn.close()

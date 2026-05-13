import hashlib
from database.db_manager import get_connection


class User:
    def __init__(self, id=None, full_name=None,
                 login=None, password=None,
                 role="user"):

        self.id = id
        self.full_name = full_name
        self.login = login
        self.password = password
        self.role = role

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        hashed_password = hashlib.sha256(
            self.password.encode()
        ).hexdigest()

        cursor.execute("""
        INSERT INTO users
        (full_name, login, password, role)
        VALUES (?, ?, ?, ?)
        """, (
            self.full_name,
            self.login,
            hashed_password,
            self.role
        ))

        self.id = cursor.lastrowid

        conn.commit()
        conn.close()


def authenticate(login, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    cursor.execute("""
    SELECT id, full_name, login,
           password, role
    FROM users
    WHERE login = ? AND password = ?
    """, (login, hashed_password))

    row = cursor.fetchone()

    conn.close()

    if row:
        return User(
            id=row[0],
            full_name=row[1],
            login=row[2],
            password=row[3],
            role=row[4]
        )

    return None


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, full_name,
           login, role
    FROM users
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()

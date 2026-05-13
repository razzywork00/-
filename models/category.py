from database.db_manager import get_connection


class Category:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO categories (name) VALUES (?)",
            (self.name,)
        )

        conn.commit()
        conn.close()


def get_all_categories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name FROM categories"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_category(category_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM categories WHERE id = ?",
        (category_id,)
    )

    conn.commit()
    conn.close()

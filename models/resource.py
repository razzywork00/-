from database.db_manager import get_connection


class Resource:
    def __init__(self, name, description,
                 category_id, status="Доступен"):
        self.name = name
        self.description = description
        self.category_id = category_id
        self.status = status

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO resources
        (name, description, category_id, status)
        VALUES (?, ?, ?, ?)
        """, (
            self.name,
            self.description,
            self.category_id,
            self.status
        ))

        conn.commit()
        conn.close()


def get_all_resources():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name, description,
           category_id, status
    FROM resources
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_resource(resource_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM resources WHERE id = ?",
        (resource_id,)
    )

    conn.commit()
    conn.close()

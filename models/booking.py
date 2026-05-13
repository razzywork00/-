from database.db_manager import get_connection


class Booking:
    def __init__(self, user_id, resource_id,
                 booking_date, start_time,
                 end_time, status="Активно"):

        self.user_id = user_id
        self.resource_id = resource_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO bookings
        (user_id, resource_id,
         booking_date, start_time,
         end_time, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            self.user_id,
            self.resource_id,
            self.booking_date,
            self.start_time,
            self.end_time,
            self.status
        ))

        conn.commit()
        conn.close()


def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, user_id, resource_id,
           booking_date, start_time,
           end_time, status
    FROM bookings
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def cancel_booking(booking_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE bookings
    SET status = 'Отменено'
    WHERE id = ?
    """, (booking_id,))

    conn.commit()
    conn.close()


def is_resource_available(resource_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM bookings
    WHERE resource_id = ?
    AND status != 'Отменено'
    """, (resource_id,))

    row = cursor.fetchone()

    conn.close()

    return row is None

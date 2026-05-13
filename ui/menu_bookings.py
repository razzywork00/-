from datetime import datetime

from models.booking import (
    Booking,
    get_all_bookings,
    cancel_booking,
    is_resource_available
)

from models.resource import get_all_resources
from models.user import get_all_users


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def validate_time(time_text):
    try:
        datetime.strptime(time_text, "%H:%M")
        return True
    except ValueError:
        return False


def menu_bookings():
    while True:
        print("\n=== Бронирования ===")
        print("1. Показать бронирования")
        print("2. Создать бронирование")
        print("3. Отменить бронирование")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            bookings = get_all_bookings()

            if not bookings:
                print("Бронирований нет")
            else:
                for b in bookings:
                    print(
                        f"ID: {b[0]} | "
                        f"Пользователь: {b[1]} | "
                        f"Ресурс: {b[2]} | "
                        f"Дата: {b[3]} | "
                        f"{b[4]}-{b[5]} | "
                        f"Статус: {b[6]}"
                    )

        elif choice == "2":
            users = get_all_users()

            print("\nПользователи:")

            for u in users:
                print(f"ID: {u[0]} | {u[1]}")

            try:
                user_id = int(input("Введите ID пользователя: "))
            except ValueError:
                print("Неверный ID")
                continue

            valid_user_ids = [u[0] for u in users]

            if user_id not in valid_user_ids:
                print("Неверный ID")
                continue

            resources = get_all_resources()

            print("\nРесурсы:")

            for r in resources:
                print(f"ID: {r[0]} | {r[1]}")

            try:
                resource_id = int(input("Введите ID ресурса: "))
            except ValueError:
                print("Неверный ID")
                continue

            valid_resource_ids = [r[0] for r in resources]

            if resource_id not in valid_resource_ids:
                print("Неверный ID")
                continue

            available = is_resource_available(resource_id)

            if not available:
                print("Ресурс уже забронирован")
                continue

            booking_date = input(
                "Дата бронирования (ДД.ММ.ГГГГ): "
            )

            if not validate_date(booking_date):
                print("Неверный формат даты")
                continue

            start_time = input(
                "Время начала (ЧЧ:ММ): "
            )

            if not validate_time(start_time):
                print("Неверный формат времени")
                continue

            end_time = input(
                "Время окончания (ЧЧ:ММ): "
            )

            if not validate_time(end_time):
                print("Неверный формат времени")
                continue

            booking = Booking(
                user_id=user_id,
                resource_id=resource_id,
                booking_date=booking_date,
                start_time=start_time,
                end_time=end_time
            )

            booking.save()

            print("Бронирование успешно создано")

        elif choice == "3":
            try:
                booking_id = int(
                    input("Введите ID бронирования: ")
                )

                cancel_booking(booking_id)

                print("Бронирование отменено")

            except ValueError:
                print("Неверный ID")

        elif choice == "0":
            break

        else:
            print("Неверный ввод")


def quick_booking():
    resources = get_all_resources()

    print("\n=== Быстрое бронирование ===")

    for r in resources:
        print(
            f"ID: {r[0]} | "
            f"{r[1]} | "
            f"Категория: {r[3]}"
        )

    print(
        "\nПерейдите в меню "
        "бронирований для создания заявки"
    )

from models.resource import (
    Resource,
    get_all_resources,
    delete_resource
)

from models.category import get_all_categories
from ui.menu_bookings import quick_booking


def menu_resources():
    while True:
        print("\n=== Ресурсы ===")
        print("1. Показать ресурсы")
        print("2. Добавить ресурс")
        print("3. Удалить ресурс")
        print("4. Быстрое бронирование")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            resources = get_all_resources()

            if not resources:
                print("Ресурсы отсутствуют")
                continue

            print("-" * 95)

            print(
                f"{'ID':<5}"
                f"{'Название':<25}"
                f"{'Описание':<30}"
                f"{'Категория':<15}"
                f"{'Статус':<15}"
            )

            print("-" * 95)

            for r in resources:
                print(
                    f"{r[0]:<5}"
                    f"{r[1]:<25}"
                    f"{r[2]:<30}"
                    f"{r[3]:<15}"
                    f"{r[4]:<15}"
                )

            print("-" * 95)

        elif choice == "2":
            categories = get_all_categories()

            print("\nКатегории:")

            for c in categories:
                print(f"ID: {c[0]} | {c[1]}")

            try:
                category_id = int(
                    input("Введите ID категории: ")
                )

                valid_ids = [c[0] for c in categories]

                if category_id not in valid_ids:
                    print("Неверный ID")
                    continue

                name = input(
                    "Введите название ресурса: "
                )

                description = input(
                    "Введите описание: "
                )

                resource = Resource(
                    name=name,
                    description=description,
                    category_id=category_id
                )

                resource.save()

                print("Ресурс успешно добавлен")

            except ValueError:
                print("Ошибка ввода")

        elif choice == "3":
            resources = get_all_resources()

            print("\nСписок ресурсов:")

            for r in resources:
                print(f"ID: {r[0]} | {r[1]}")

            try:
                resource_id = int(
                    input("Введите ID ресурса: ")
                )

                valid_ids = [r[0] for r in resources]

                if resource_id not in valid_ids:
                    print("Неверный ID")
                    continue

                delete_resource(resource_id)

                print("Ресурс удалён")

            except ValueError:
                print("Ошибка ввода")

        elif choice == "4":
            quick_booking()

        elif choice == "0":
            break

        else:
            print("Неверный ввод")

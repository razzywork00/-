from models.category import (
    Category,
    get_all_categories,
    delete_category
)

from models.resource import get_all_resources


def menu_categories():
    while True:
        print("\n=== Управление категориями ===")
        print("1. Показать категории")
        print("2. Добавить категорию")
        print("3. Удалить категорию")
        print("4. Просмотр ресурсов категории")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            categories = get_all_categories()

            if not categories:
                print("Категории отсутствуют")
                continue

            for c in categories:
                print(f"ID: {c[0]} | {c[1]}")

        elif choice == "2":
            name = input(
                "Введите название категории: "
            )

            category = Category(name)

            category.save()

            print("Категория добавлена")

        elif choice == "3":
            categories = get_all_categories()

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

                delete_category(category_id)

                print("Категория удалена")

            except ValueError:
                print("Ошибка ввода")

        elif choice == "4":
            categories = get_all_categories()

            for c in categories:
                print(f"ID: {c[0]} | {c[1]}")

            try:
                category_id = int(
                    input(
                        "Введите ID категории: "
                    )
                )

                valid_ids = [c[0] for c in categories]

                if category_id not in valid_ids:
                    print("Неверный ID")
                    continue

                resources = get_all_resources()

                print("\nРесурсы категории:")

                found = False

                for r in resources:
                    if r[3] == category_id:
                        found = True

                        print(
                            f"ID: {r[0]} | "
                            f"{r[1]} | "
                            f"{r[2]}"
                        )

                if not found:
                    print(
                        "В данной категории "
                        "ресурсов нет"
                    )

            except ValueError:
                print("Ошибка ввода")

        elif choice == "0":
            break

        else:
            print("Неверный ввод")

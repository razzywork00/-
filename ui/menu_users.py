from models.user import (
    User,
    get_all_users,
    delete_user
)


def menu_users():
    while True:
        print("\n=== Управление пользователями ===")
        print("1. Показать пользователей")
        print("2. Добавить пользователя")
        print("3. Удалить пользователя")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            users = get_all_users()

            if not users:
                print("Пользователи отсутствуют")
                continue

            print("-" * 70)

            print(
                f"{'ID':<5}"
                f"{'ФИО':<25}"
                f"{'Логин':<20}"
                f"{'Роль':<15}"
            )

            print("-" * 70)

            for u in users:
                print(
                    f"{u[0]:<5}"
                    f"{u[1]:<25}"
                    f"{u[2]:<20}"
                    f"{u[3]:<15}"
                )

            print("-" * 70)

        elif choice == "2":
            full_name = input("Введите ФИО: ")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            user = User(
                full_name=full_name,
                login=login,
                password=password
            )

            user.save()

            print(
                f"Пользователь добавлен. "
                f"ID: {user.id}"
            )

        elif choice == "3":
            users = get_all_users()

            for u in users:
                print(f"ID: {u[0]} | {u[1]}")

            try:
                user_id = int(
                    input("Введите ID пользователя: ")
                )

                valid_ids = [u[0] for u in users]

                if user_id not in valid_ids:
                    print("Неверный ID")
                    continue

                delete_user(user_id)

                print("Пользователь удалён")

            except ValueError:
                print("Ошибка ввода")

        elif choice == "0":
            break

        else:
            print("Неверный ввод")

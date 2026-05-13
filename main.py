from database.db_manager import initialize_db

from ui.menu import show_main_menu
from ui.menu_resources import menu_resources
from ui.menu_bookings import menu_bookings
from ui.menu_users import menu_users
from ui.menu_categories import menu_categories

from models.user import User, authenticate


def register():
    print("\n=== Регистрация ===")

    full_name = input("ФИО: ")
    login = input("Логин: ")
    password = input("Пароль: ")

    user = User(
        full_name=full_name,
        login=login,
        password=password
    )

    user.save()

    print(f"Регистрация завершена. Ваш ID: {user.id}")


def login_system():
    print("\n=== Вход ===")

    login = input("Логин: ")
    password = input("Пароль: ")

    user = authenticate(login, password)

    if user:
        print(f"Добро пожаловать, {user.full_name}")
        return user

    print("Неверный логин или пароль")
    return None


def main():
    initialize_db()

    current_user = None

    while True:
        print("\n=== Авторизация ===")
        print("1. Вход")
        print("2. Регистрация")
        print("0. Выход")

        auth_choice = input("Выберите действие: ")

        if auth_choice == "1":
            current_user = login_system()

            if current_user:

                while True:
                    user_choice = show_main_menu()

                    if user_choice == "1":
                        menu_resources()

                    elif user_choice == "2":
                        menu_bookings()

                    elif user_choice == "3":
                        menu_users()

                    elif user_choice == "4":
                        menu_categories()

                    elif user_choice == "0":
                        print(
                            f"Ждём вас снова, "
                            f"{current_user.login}!"
                        )
                        break

                    else:
                        print("Неверный ввод")

        elif auth_choice == "2":
            register()

        elif auth_choice == "0":
            if current_user:
                print(
                    f"Ждём вас снова, "
                    f"{current_user.login}!"
                )
            else:
                print("До свидания!")
            break

        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()

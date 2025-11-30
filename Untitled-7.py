class UserAccount:
    def __init__(self, username, email, password):
        """
        Конструктор класса UserAccount
        :param username: имя пользователя
        :param email: электронная почта
        :param password: пароль (будет храниться как приватный атрибут)
        """
        self.username = username
        self.email = email
        self.__password = password  # приватный атрибут
    
    def set_password(self, new_password):
        """
        Безопасно изменяет пароль аккаунта
        :param new_password: новый пароль
        """
        if self._validate_password(new_password):
            self.__password = new_password
            print("✓ Пароль успешно изменен!")
            return True
        else:
            print("✗ Ошибка: пароль не соответствует требованиям безопасности")
            return False
    
    def check_password(self, password):
        """
        Проверяет, соответствует ли введённый пароль текущему паролю
        :param password: пароль для проверки
        :return: True если пароль верный, иначе False
        """
        return password == self.__password
    
    def _validate_password(self, password):
        """
        Внутренний метод для проверки сложности пароля
        :param password: пароль для проверки
        :return: True если пароль соответствует требованиям
        """
        if len(password) < 6:
            print("✗ Пароль должен содержать минимум 6 символов")
            return False
        return True
    
    def get_account_info(self):
        """
        Возвращает публичную информацию об аккаунте (без пароля)
        :return: строка с информацией об аккаунте
        """
        return f"Имя пользователя: {self.username}, Email: {self.email}"
    
    def __str__(self):
        """Строковое представление объекта"""
        return self.get_account_info()

def get_input(prompt, password=False):
    """
    Функция для получения ввода от пользователя
    :param prompt: подсказка для ввода
    :param password: если True, скрывает ввод (для пароля)
    :return: введенная строка
    """
    if password:
        import getpass
        return getpass.getpass(prompt)
    else:
        return input(prompt)

def create_account():
    """
    Функция для создания нового аккаунта через терминал
    :return: объект UserAccount
    """
    print("\n" + "="*50)
    print("СОЗДАНИЕ НОВОГО АККАУНТА")
    print("="*50)
    
    username = input("Введите имя пользователя: ").strip()
    while not username:
        print("✗ Имя пользователя не может быть пустым")
        username = input("Введите имя пользователя: ").strip()
    
    email = input("Введите email: ").strip()
    while not email:
        print("✗ Email не может быть пустым")
        email = input("Введите email: ").strip()
    
    password = get_input("Введите пароль: ", password=True)
    while not password:
        print("✗ Пароль не может быть пустым")
        password = get_input("Введите пароль: ", password=True)
    
    confirm_password = get_input("Подтвердите пароль: ", password=True)
    
    while password != confirm_password:
        print("✗ Пароли не совпадают! Попробуйте еще раз.")
        password = get_input("Введите пароль: ", password=True)
        confirm_password = get_input("Подтвердите пароль: ", password=True)
    
    # Создаем аккаунт
    account = UserAccount(username, email, password)
    print("\n✓ Аккаунт успешно создан!")
    print(account.get_account_info())
    
    return account

def change_password_menu(account):
    """
    Меню для изменения пароля
    :param account: объект UserAccount
    """
    print("\n" + "="*50)
    print("ИЗМЕНЕНИЕ ПАРОЛЯ")
    print("="*50)
    
    # Проверяем текущий пароль
    current_password = get_input("Введите текущий пароль: ", password=True)
    if not account.check_password(current_password):
        print("✗ Неверный текущий пароль!")
        return
    
    # Запрашиваем новый пароль
    new_password = get_input("Введите новый пароль: ", password=True)
    while not new_password:
        print("✗ Пароль не может быть пустым")
        new_password = get_input("Введите новый пароль: ", password=True)
    
    confirm_new_password = get_input("Подтвердите новый пароль: ", password=True)
    
    if new_password != confirm_new_password:
        print("✗ Новые пароли не совпадают!")
        return
    
    # Пытаемся установить новый пароль
    if account.set_password(new_password):
        print("✓ Пароль успешно изменен!")

def check_password_menu(account):
    """
    Меню для проверки пароля
    :param account: объект UserAccount
    """
    print("\n" + "="*50)
    print("ПРОВЕРКА ПАРОЛЯ")
    print("="*50)
    
    password_to_check = get_input("Введите пароль для проверки: ", password=True)
    
    if account.check_password(password_to_check):
        print("✓ Пароль верный!")
    else:
        print("✗ Пароль неверный!")

def main_menu(account):
    """
    Главное меню программы
    :param account: объект UserAccount
    """
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print(f"Текущий аккаунт: {account.username} ({account.email})")
        print("\nВыберите действие:")
        print("1 - Показать информацию об аккаунте")
        print("2 - Проверить пароль")
        print("3 - Изменить пароль")
        print("4 - Создать новый аккаунт")
        print("0 - Выйти из программы")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "1":
            print("\n" + "-"*30)
            print("ИНФОРМАЦИЯ ОБ АККАУНТЕ")
            print("-"*30)
            print(account.get_account_info())
        
        elif choice == "2":
            check_password_menu(account)
        
        elif choice == "3":
            change_password_menu(account)
        
        elif choice == "4":
            new_account = create_account()
            if new_account:
                account = new_account
                print(f"\n✓ Переключение на новый аккаунт: {account.username}")
        
        elif choice == "0":
            print("\nДо свидания!")
            break
        
        else:
            print("✗ Неверный выбор! Попробуйте еще раз.")

def main():
    """
    Основная функция программы
    """
    print("="*60)
    print("СИСТЕМА УПРАВЛЕНИЯ АККАУНТАМИ ПОЛЬЗОВАТЕЛЕЙ")
    print("="*60)
    
    # Создаем начальный аккаунт
    print("\nДля начала работы создайте ваш первый аккаунт:")
    account = create_account()
    
    main_menu(account)

if __name__ == "__main__":
    main()
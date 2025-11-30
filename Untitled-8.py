class Vehicle:
    def __init__(self, make, model):
        """
        Базовый класс Vehicle
        :param make: марка транспортного средства
        :param model: модель транспортного средства
        """
        self.make = make
        self.model = model
    
    def get_info(self):
        """
        Возвращает информацию о транспортном средстве
        :return: строка с информацией
        """
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        """
        Класс Car, наследующий от Vehicle
        :param make: марка автомобиля
        :param model: модель автомобиля
        :param fuel_type: тип топлива
        """
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        """
        Переопределенный метод, включающий информацию о типе топлива
        :return: строка с полной информацией об автомобиле
        """
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

def create_vehicle():
    """Функция для создания транспортного средства через ввод пользователя"""
    print("\n" + "=" * 40)
    print("СОЗДАНИЕ ТРАНСПОРТНОГО СРЕДСТВА")
    print("=" * 40)
    
    make = input("Введите марку транспортного средства: ").strip()
    while not make:
        print("Марка не может быть пустой!")
        make = input("Введите марку транспортного средства: ").strip()
    
    model = input("Введите модель транспортного средства: ").strip()
    while not model:
        print("Модель не может быть пустой!")
        model = input("Введите модель транспортного средства: ").strip()
    
    return make, model

def create_car():
    """Функция для создания автомобиля через ввод пользователя"""
    print("\n" + "=" * 40)
    print("СОЗДАНИЕ АВТОМОБИЛЯ")
    print("=" * 40)
    
    make = input("Введите марку автомобиля: ").strip()
    while not make:
        print("Марка не может быть пустой!")
        make = input("Введите марку автомобиля: ").strip()
    
    model = input("Введите модель автомобиля: ").strip()
    while not model:
        print("Модель не может быть пустой!")
        model = input("Введите модель автомобиля: ").strip()
    
    print("\nДоступные типы топлива:")
    print("1 - бензин")
    print("2 - дизель") 
    print("3 - электричество")
    print("4 - гибрид")
    print("5 - другой")
    
    fuel_choice = input("Выберите тип топлива (1-5): ").strip()
    fuel_types = {
        '1': 'бензин',
        '2': 'дизель',
        '3': 'электричество',
        '4': 'гибрид',
        '5': 'другой'
    }
    
    fuel_type = fuel_types.get(fuel_choice, 'другой')
    
    return make, model, fuel_type

def main():
    """Основная функция программы"""
    print("=" * 50)
    print("СИСТЕМА УЧЕТА ТРАНСПОРТНЫХ СРЕДСТВ")
    print("=" * 50)
    
    vehicles = []  # Список для хранения всех транспортных средств
    
    while True:
        print("\n" + "=" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1 - Создать транспортное средство (Vehicle)")
        print("2 - Создать автомобиль (Car)")
        print("3 - Показать все транспортные средства")
        print("4 - Выйти из программы")
        
        choice = input("\nВыберите действие (1-4): ").strip()
        
        if choice == "1":
            make, model = create_vehicle()
            vehicle = Vehicle(make, model)
            vehicles.append(vehicle)
            print(f"\n✓ Создано транспортное средство: {vehicle.get_info()}")
            
        elif choice == "2":
            make, model, fuel_type = create_car()
            car = Car(make, model, fuel_type)
            vehicles.append(car)
            print(f"\n✓ Создан автомобиль: {car.get_info()}")
            
        elif choice == "3":
            if not vehicles:
                print("\n✗ Нет созданных транспортных средств")
            else:
                print("\n" + "=" * 40)
                print("СПИСОК ТРАНСПОРТНЫХ СРЕДСТВ")
                print("=" * 40)
                for i, vehicle in enumerate(vehicles, 1):
                    print(f"{i}. {vehicle.get_info()}")
                    print(f"   Тип: {type(vehicle).__name__}")
                    print()
                    
        elif choice == "4":
            print("\nДо свидания!")
            break
            
        else:
            print("\n✗ Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()

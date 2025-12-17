class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id
    
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.subordinates = []
    
    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"
    
    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization
    
    def perform_maintenance(self, equipment):
        return f"Техник {self.name} выполняет обслуживание: {equipment}"
    
    def get_info(self):
        return f"Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []
    
    def add_employee(self, employee):
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду {self.name}"
    
    def get_team_info(self):
        if not self.team:
            return f"У {self.name} нет подчинённых в команде"
        
        team_info = f"Команда менеджера {self.name}:\n"
        for i, employee in enumerate(self.team, 1):
            team_info += f"{i}. {employee.get_info()}\n"
        return team_info
    
    def get_info(self):
        return f"Технический менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}"


def create_employee():
    print("\nСоздание обычного сотрудника:")
    name = input("Введите имя: ")
    emp_id = input("Введите ID: ")
    return Employee(name, emp_id)


def create_manager():
    print("\nСоздание менеджера:")
    name = input("Введите имя: ")
    emp_id = input("Введите ID: ")
    department = input("Введите отдел: ")
    return Manager(name, emp_id, department)


def create_technician():
    print("\nСоздание техника:")
    name = input("Введите имя: ")
    emp_id = input("Введите ID: ")
    specialization = input("Введите специализацию: ")
    return Technician(name, emp_id, specialization)


def create_tech_manager():
    print("\nСоздание технического менеджера:")
    name = input("Введите имя: ")
    emp_id = input("Введите ID: ")
    department = input("Введите отдел: ")
    specialization = input("Введите специализацию: ")
    return TechManager(name, emp_id, department, specialization)


def main():
    employees = []
    managers = []
    technicians = []
    tech_managers = []
    
    while True:
        print("\n" + "=" * 50)
        print("МЕНЮ УПРАВЛЕНИЯ СОТРУДНИКАМИ")
        print("=" * 50)
        print("1. Создать обычного сотрудника")
        print("2. Создать менеджера")
        print("3. Создать техника")
        print("4. Создать технического менеджера")
        print("5. Показать всех сотрудников")
        print("6. Управлять командой технического менеджера")
        print("7. Выполнить действия (управление проектом, обслуживание)")
        print("8. Выйти")
        
        choice = input("\nВыберите действие (1-8): ")
        
        if choice == "1":
            emp = create_employee()
            employees.append(emp)
            print(f"\nСоздан: {emp.get_info()}")
            
        elif choice == "2":
            mgr = create_manager()
            managers.append(mgr)
            print(f"\nСоздан: {mgr.get_info()}")
            
        elif choice == "3":
            tech = create_technician()
            technicians.append(tech)
            print(f"\nСоздан: {tech.get_info()}")
            
        elif choice == "4":
            tm = create_tech_manager()
            tech_managers.append(tm)
            print(f"\nСоздан: {tm.get_info()}")
            
        elif choice == "5":
            print("\n" + "=" * 30)
            print("ВСЕ СОТРУДНИКИ")
            print("=" * 30)
            
            if employees:
                print("\nОбычные сотрудники:")
                for emp in employees:
                    print(f"  - {emp.get_info()}")
            
            if managers:
                print("\nМенеджеры:")
                for mgr in managers:
                    print(f"  - {mgr.get_info()}")
            
            if technicians:
                print("\nТехники:")
                for tech in technicians:
                    print(f"  - {tech.get_info()}")
            
            if tech_managers:
                print("\nТехнические менеджеры:")
                for tm in tech_managers:
                    print(f"  - {tm.get_info()}")
            
            if not any([employees, managers, technicians, tech_managers]):
                print("Нет созданных сотрудников")
                
        elif choice == "6":
            if not tech_managers:
                print("\nНет технических менеджеров. Создайте сначала.")
                continue
                
            print("\nВыберите технического менеджера:")
            for i, tm in enumerate(tech_managers, 1):
                print(f"{i}. {tm.name}")
            
            try:
                tm_index = int(input("Номер: ")) - 1
                if 0 <= tm_index < len(tech_managers):
                    tm = tech_managers[tm_index]
                    
                    print(f"\nУправление командой для {tm.name}")
                    print("1. Добавить сотрудника в команду")
                    print("2. Показать команду")
                    
                    sub_choice = input("Выберите действие: ")
                    
                    if sub_choice == "1":
                        all_people = employees + managers + technicians
                        print("\nДоступные сотрудники:")
                        for i, person in enumerate(all_people, 1):
                            print(f"{i}. {person.get_info()}")
                        
                        if all_people:
                            person_index = int(input("Номер сотрудника для добавления: ")) - 1
                            if 0 <= person_index < len(all_people):
                                print(tm.add_employee(all_people[person_index]))
                            else:
                                print("Неверный номер")
                        else:
                            print("Нет доступных сотрудников")
                            
                    elif sub_choice == "2":
                        print(f"\n{tm.get_team_info()}")
                    else:
                        print("Неверный выбор")
                else:
                    print("Неверный номер")
            except ValueError:
                print("Введите число")
                
        elif choice == "7":
            print("\nВыполнение действий:")
            print("1. Менеджер управляет проектом")
            print("2. Техник выполняет обслуживание")
            print("3. Технический менеджер выполняет оба действия")
            
            action_choice = input("Выберите действие (1-3): ")
            
            if action_choice == "1":
                if managers:
                    print("\nВыберите менеджера:")
                    for i, mgr in enumerate(managers, 1):
                        print(f"{i}. {mgr.name}")
                    
                    mgr_index = int(input("Номер: ")) - 1
                    if 0 <= mgr_index < len(managers):
                        project = input("Введите название проекта: ")
                        print(managers[mgr_index].manage_project(project))
                    else:
                        print("Неверный номер")
                else:
                    print("Нет созданных менеджеров")
                    
            elif action_choice == "2":
                if technicians:
                    print("\nВыберите техника:")
                    for i, tech in enumerate(technicians, 1):
                        print(f"{i}. {tech.name}")
                    
                    tech_index = int(input("Номер: ")) - 1
                    if 0 <= tech_index < len(technicians):
                        equipment = input("Введите оборудование для обслуживания: ")
                        print(technicians[tech_index].perform_maintenance(equipment))
                    else:
                        print("Неверный номер")
                else:
                    print("Нет созданных техников")
                    
            elif action_choice == "3":
                if tech_managers:
                    print("\nВыберите технического менеджера:")
                    for i, tm in enumerate(tech_managers, 1):
                        print(f"{i}. {tm.name}")
                    
                    tm_index = int(input("Номер: ")) - 1
                    if 0 <= tm_index < len(tech_managers):
                        project = input("Введите название проекта: ")
                        equipment = input("Введите оборудование для обслуживания: ")
                        
                        tm = tech_managers[tm_index]
                        print(f"\n{tm.manage_project(project)}")
                        print(tm.perform_maintenance(equipment))
                    else:
                        print("Неверный номер")
                else:
                    print("Нет созданных технических менеджеров")
            else:
                print("Неверный выбор")
                
        elif choice == "8":
            print("Выход из программы.")
            break
            
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

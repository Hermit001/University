# Определение класса Car
class Car:
    # Конструктор класса Car, инициализирует атрибуты цвет, тип и год
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        self.engine_status = False  # Статус двигателя (заведен/заглушен)

    # Метод для запуска автомобиля
    def start(self):
        if not self.engine_status:  # Проверка, не заведен ли автомобиль
            self.engine_status = True
            print("Автомобиль заведен")
        else:
            print("Автомобиль уже заведен")

    # Метод для отключения автомобиля
    def stop(self):
        if self.engine_status:  # Проверка, заведен ли автомобиль
            self.engine_status = False
            print("Автомобиль заглушен")
        else:
            print("Автомобиль уже заглушен")

    # Метод для установки года выпуска автомобиля
    def set_year(self, new_year):
        self.year = new_year

    # Метод для установки типа автомобиля
    def set_type(self, new_type):
        self.type = new_type

    # Метод для установки цвета автомобиля
    def set_color(self, new_color):
        self.color = new_color

# Создание объекта класса Car с начальными параметрами
my_car = Car("синий", "седан", 2020)

# Основной цикл программы
while True:
    # Вывод меню для пользователя
    print("\nВыберите действие:")
    print("1. Запустить автомобиль")
    print("2. Остановить автомобиль")
    print("3. Присвоить год выпуска")
    print("4. Присвоить тип")
    print("5. Выйти")

    # Запрос выбора у пользователя
    choice = input("Введите номер действия: ")

    if choice == "1":
        my_car.start()
    elif choice == "2":
        my_car.stop()
    elif choice == "3":
        new_year = input("Введите новый год выпуска: ")
        my_car.set_year(new_year)
    elif choice == "4":
        new_type = input("Введите новый тип: ")
        my_car.set_type(new_type)
    elif choice == "5":
        # Вывод характеристик автомобиля перед выходом
        print(f"\nХарактеристики автомобиля:")
        print(f"Цвет: {my_car.color}")
        print(f"Тип: {my_car.type}")
        print(f"Год выпуска: {my_car.year}")
        break  # Выход из цикла при выборе "Выйти"
    else:
        print("Неверный выбор. Пожалуйста, выберите действие из списка.")

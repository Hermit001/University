class Sphere:
    def __init__(self):
        # Запрос радиуса и координат центра у пользователя
        self.radius = float(input("Введите радиус сферы: "))
        self.x = float(input("Введите координату X центра сферы: "))
        self.y = float(input("Введите координату Y центра сферы: "))
        self.z = float(input("Введите координату Z центра сферы: "))

    def get_volume(self):
        # Реализация метода get_volume
        return (4/3) * 3.14159265359 * self.radius**3

    def get_square(self):
        # Реализация метода get_square
        return 4 * 3.14159265359 * self.radius**2

    def get_radius(self):
        # Реализация метода get_radius
        return self.radius

    def get_center(self):
        # Реализация метода get_center
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        # Реализация метода set_radius
        self.radius = r

    def set_center(self, x, y, z):
        # Реализация метода set_center
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        # Реализация метода is_point_inside
        distance = ((x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2)**0.5
        return distance <= self.radius

# Создаем объект сферы с данными, введенными пользователем
my_sphere = Sphere()

# Выводим радиус и координаты центра сферы
print("Радиус сферы:", my_sphere.get_radius())
print("Координаты центра сферы:", my_sphere.get_center())

# Вычисляем и выводим объем и площадь сферы
print("Объем сферы:", my_sphere.get_volume())
print("Площадь поверхности сферы:", my_sphere.get_square())

# Запрашиваем новый радиус и устанавливаем его
new_radius = float(input("Введите новый радиус сферы: "))
my_sphere.set_radius(new_radius)

# Выводим радиус после изменения
print("Новый радиус сферы:", my_sphere.get_radius())

# Запрашиваем новые координаты центра и устанавливаем их
new_x = float(input("Введите новую координату X центра сферы: "))
new_y = float(input("Введите новую координату Y центра сферы: "))
new_z = float(input("Введите новую координату Z центра сферы: "))
my_sphere.set_center(new_x, new_y, new_z)

# Выводим новые координаты центра
print("Новые координаты центра сферы:", my_sphere.get_center())

# Запрашиваем координаты точки и проверяем, находится ли она внутри сферы
point_x = float(input("Введите координату X точки: "))
point_y = float(input("Введите координату Y точки: "))
point_z = float(input("Введите координату Z точки: "))
if my_sphere.is_point_inside(point_x, point_y, point_z):
    print("Точка находится внутри сферы.")
else:
    print("Точка находится снаружи сферы.")

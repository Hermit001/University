class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Reviewer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка при выставлении оценки"

class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.calculate_average_grade()}"

    def calculate_average_grade(self):
        total_grade = 0
        count = 0
        for grades in self.grades.values():
            total_grade += sum(grades)
            count += len(grades)
        if count > 0:
            return round(total_grade / count, 1)
        else:
            return 0

class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        if self.grades:
            average_grade = sum(sum(grades) for grades in self.grades.values()) / len(self.grades)
        else:
            average_grade = 0
        return super().__str__() + f"\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка при выставлении оценки"


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        if self.grades:
            average_grade = sum(sum(grades) for grades in self.grades.values()) / len(self.grades)
        else:
            average_grade = 0
        return super().__str__() + f"\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка при выставлении оценки"

def average_grade_for_course(students, course_name):
    total_grade = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    if count > 0:
        return round(total_grade / count, 1)
    else:
        return 0

def average_grade_for_lectures(lecturers, course_name):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grade += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    if count > 0:
        return round(total_grade / count, 1)
    else:
        return 0

# Создаем студентов
student1 = Student('Ruoy', 'Eman')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('Введение в программирование')

student2 = Student('John', 'Doe')
student2.courses_in_progress.append('Git')
student2.finished_courses.append('Python')

# Создаем лекторов
lecturer1 = Lecturer('Some', 'Lecturer')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer('Another', 'Lecturer')
lecturer2.courses_attached.append('Git')

# Создаем ревьюеров
reviewer1 = Reviewer('Some', 'Reviewer')
reviewer1.courses_attached.append('Python')

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached.append('Git')

# Выставляем оценки студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 7)

# Выставляем оценки лекторам
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Git', 10)

# Выводим информацию
print("Информация о студентах:")
print(student1)
print("\n")
print(student2)
print("\n")

print("Информация о лекторах:")
print(lecturer1)
print("\n")
print(lecturer2)
print("\n")

print("Информация о ревьюерах:")
print(reviewer1)
print("\n")
print(reviewer2)
print("\n")

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_grade_for_course([student1, student2], 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Git': {average_grade_for_lectures([lecturer1, lecturer2], 'Git')}")

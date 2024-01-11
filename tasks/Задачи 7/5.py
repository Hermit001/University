# Считываем количество файлов
n = int(input())

# Создаем словарь для хранения допустимых операций по каждому файлу
file_permissions = {}

# Считываем информацию о файлах и их допустимых операциях
for _ in range(n):
    file_info = input().split()
    file_name = file_info[0]
    operations = file_info[1:]
    file_permissions[file_name] = operations

# Считываем количество операций
m = int(input())

# Создаем список для хранения ответов
answers = []

# Считываем операции и проверяем их допустимость
for _ in range(m):
    operation_info = input().split()
    operation = operation_info[0]
    file_name = operation_info[1]
    
    # Проверяем, есть ли такой файл в словаре
    if file_name in file_permissions:
        # Если операция допустима для файла, добавляем "Ok" в список ответов
        if operation in file_permissions[file_name]:
            answers.append("Ok")
        # Иначе добавляем "Denied" в список ответов
        else:
            answers.append("Denied")
    # Если файла нет в словаре, добавляем "Denied" в список ответов
    else:
        answers.append("Denied")

# Выводим все ответы в конце
for answer in answers:
    print(answer)

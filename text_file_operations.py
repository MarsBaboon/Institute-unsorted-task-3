import re
import os
import string
import random

# Открываем файл A.txt в режиме записи
with open('A.txt', 'w') as file:
    # Записываем текст в файл
    file.write('Привет, мир!')
    
print("Файл A.txt создан.")

# Открываем файл A.txt в режиме чтения
with open('A.txt', 'r') as file:
    # Читаем содержимое файла
    content = file.read()
    
print("Содержимое файла A.txt:")
print(content)

# Считываем текст из исходного файла
with open('исходный_файл.txt', 'r') as source_file:
    text = source_file.read()

# Записываем текст в файл A.txt
with open('A.txt', 'w') as file:
    file.write(text)

print("Файл A.txt перезаписан текстом из файла исходный_файл.txt.")

# Производим поиск в файле A.txt с использованием регулярных выражений
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'  # Замените на ваше регулярное выражение

with open('A.txt', 'r') as file:
    content = file.read()
    matches = re.findall(pattern, content)

# Выводим результаты поиска
print("Результаты поиска в файле A.txt:")
for match in matches:
    print(match)

# Создаем новую директорию
new_directory = 'Новая_директория'

# Проверяем, существует ли уже директория с таким именем
if not os.path.exists(new_directory):
    # Создаем новую директорию
    os.mkdir(new_directory)
    print(f"Создана новая директория: {new_directory}")
else:
    print(f"Директория {new_directory} уже существует.")

source_file = 'A.txt'
destination_dir = 'Новая_директория'
# Запросить количество копий
n = int(input("Введите количество копий для создания: "))

for i in range(1, n+1):
    copy_file_name = f"A_copy{i}.txt"
    copy_file_path = os.path.join(destination_dir, copy_file_name)
    
    with open(source_file, 'rb') as src_file, open(copy_file_path, 'wb') as dest_file:
        dest_file.write(src_file.read())
    
    print(f"Создана копия {copy_file_name} в {copy_file_path}")

# Запросить путь к директории
directory = destination_dir

# Получить список файлов в директории
file_list = os.listdir(directory)

# Проверить, есть ли файлы в директории
if not file_list:
    print("В директории нет файлов. Переименовывание будет пропущено")
else:
    # Посчитать количество файлов
    num_files = len(file_list)

    # Создать список заглавных букв латинского алфавита
    alphabet = string.ascii_uppercase

    # Отсортировать список файлов по числам в конце названия
    file_list.sort(key=lambda x: int(x.split('_')[1][4:].split('.')[0]))

    # Переименовать файлы
    for i, file_name in enumerate(file_list):
        # Генерировать комбинацию из букв
        combo = ""
        div = i
        while div >= 0:
            mod = div % len(alphabet)
            combo = alphabet[mod] + combo
            div = (div // len(alphabet)) - 1

        new_file_name = combo + os.path.splitext(file_name)[1]
        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)
        
        os.rename(old_file_path, new_file_path)
        print(f"Переименован файл {file_name} в {new_file_name}")
    
    file_list = os.listdir(directory)

    # Очистить содержимое файлов
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        
        # Проверить, является ли объект файлом
        if os.path.isfile(file_path):
            with open(file_path, 'w') as file:
                file.truncate(0)  # Очистить содержимое файла

            print(f"Очищен файл {file_name}")

# Запросить путь к исходному файлу
source_file_path = 'исходный_файл.txt'

# Проверить, существует ли исходный файл
if not os.path.isfile(source_file_path):
    print("Исходный файл не существует.")
else:
    # Получить список файлов в директории
    file_list = os.listdir(directory)

    # Проверить, есть ли файлы в директории
    if not file_list:
        print("В директории нет файлов.")
    else:
        # Открыть исходный файл для чтения
        with open(source_file_path, 'r') as source_file:
            source_text = source_file.read().split()

            # Заполнить каждый файл случайным числом слов из исходного файла
            for file_name in file_list:
                file_path = os.path.join(directory, file_name)

                # Проверить, является ли объект файлом
                if os.path.isfile(file_path):
                    num_words = random.randint(1, len(source_text))
                    random_words = ' '.join(random.sample(source_text, num_words))

                    with open(file_path, 'w') as file:
                        file.write(random_words)

                    print(f"Заполнен файл {file_name} случайным числом слов ({num_words})")

            print(f"Число слов в исходном файле: {len(source_text)}")

            # Удалить файлы с числом слов менее 50% от числа слов в исходном файле
            for file_name in file_list:
                file_path = os.path.join(directory, file_name)
                # Проверить, является ли объект файлом
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as file:
                        file_text = file.read().split()
                        file.close()
                        if len(file_text) < 0.5 * len(source_text):
                            os.remove(file_path)
                            print(f"Удален файл {file_name} (Число слов: {len(file_text)})")
                        else:
                            print(f"Файл {file_name} (Число слов: {len(file_text)}) соответствует условию")

input()

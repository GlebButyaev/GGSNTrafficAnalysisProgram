import os
import datetime
import timeit

start_time = timeit.default_timer()

# Функция для получения предыдущей даты

def get_previous_date():
    current_date = datetime.datetime.now()
    previous_date = current_date - datetime.timedelta(days=1)
    return previous_date.date()

# Получаем предыдущую дату в формате ГГГГММДД
previous_date = get_previous_date().strftime("%Y%m%d")

print(previous_date)

# Функция для поиска строк и копирования их содержимого
def find_and_copy_lines(directory, search_date):
    count_bytes = dict()

    # Обходим все файлы в указанной директори
    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_date in file:
                file_path = os.path.join(root, file)

                # Открываем каждый файл для чтения
                with open(file_path, 'r') as f:
                    for line in f:
                        line = line.split(';')

                        # Если значение во второй колонке равно 'delete', выполняем дальнейшие действия
                        if line[1]=='delete':
                            dict_key = line [0][:-12]  + '    ' + line [11] + '    ' + line [12]
                            # Подсчитываем сумму байтов для каждого уникального ключа
                            if dict_key not in count_bytes:
                                count_bytes[dict_key] = int(line[24]) + int(line[27])
                            else:
                                 count_bytes[dict_key] += int(line[24]) + int(line[27]) 
    # Выводим словарь с результатами подсчета                              
    print(count_bytes)                                          

    # Создаем/открываем файл для записи            
    with open(f'pgwX_daily.traff_{get_previous_date().strftime("%Y%m")}.txt', 'a') as output_file:
        # Записываем результаты подсчета в файл
        for key,i in count_bytes.items():
            c = f"{key}    {i}"
            output_file.writelines(c)
            output_file.write('\n')
        output_file.write('\n')    

# Путь к директории, в которой будем искать файлы    
directory_path = r"C:\Users\gleb.butyaev\Desktop\Файлы"

# Вызываем функцию поиска и копирования строк с указанной датой 
find_and_copy_lines(directory_path, previous_date)

end_time = timeit.default_timer()
execution_time = end_time - start_time

print(f"Время выполнения программы: {execution_time} секунд")


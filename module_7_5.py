import os
import time


directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        f_path = os.path.join(root, file)
        f_time = os.path.getmtime(f_path)
        format_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(f_time))
        f_size = os.path.getsize(f_path)
        parent_dir = os.path.dirname(f_path)
        print(f'Найден файл: "{file}", расположен в "{f_path}", размер: {f_size}, байт. '
              f'Время изменения {format_time}. Родительская директория {parent_dir}')

"""
*(вместо 4) Написать скрипт, который выводит статистику для заданной папки
в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""
import os
import json

out_dict = {}
list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []
list_1000000 = []
for root, dir, files in os.walk('some_data'):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 100:
            file_ext = file.split('.')[1]
            list_100.append(file_ext)
            out_dict[100] = (len(list_100),list(set(list_100)))
        elif os.stat(os.path.join(root, file)).st_size <= 1000:
            file_ext = file.split('.')[1]
            list_1000.append(file_ext)
            out_dict[1000] = (len(list_1000), list(set(list_1000)))
        elif os.stat(os.path.join(root, file)).st_size <= 10000:
            file_ext = file.split('.')[1]
            list_10000.append(file_ext)
            out_dict[10000] = (len(list_10000), list(set(list_10000)))
        elif os.stat(os.path.join(root, file)).st_size <= 100000:
            file_ext = file.split('.')[1]
            list_100000.append(file_ext)
            out_dict[100000] = (len(list_100000), list(set(list_100000)))
        else:
            file_ext = file.split('.')[1]
            list_1000000.append(file_ext)
            out_dict[1000000] = (len(list_1000000), list(set(list_1000000)))

print(out_dict)

with open('some_data_summary.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f)
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

#через цикл
out_dict = {}
list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []
list_10000000 = []
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
            list_10000000.append(file_ext)
            out_dict[10000000] = (len(list_10000000), list(set(list_10000000)))

print(out_dict)

with open('some_data_summary.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f)

#через list compreheinsion
list_100_size = [file.split('.')[1] for root, dir, files in os.walk('some_data') for file in files
                 if os.stat(os.path.join(root, file)).st_size <= 100]
list_1000_size = [file.split('.')[1] for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 1000
                  and os.stat(os.path.join(root, file)).st_size > 100]
list_10000_size = [file.split('.')[1] for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 10000
                  and os.stat(os.path.join(root, file)).st_size > 1000]
list_100000_size = [file.split('.')[1] for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 100000
                  and os.stat(os.path.join(root, file)).st_size > 10000]
list_1000000_size = [file.split('.')[1] for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 1000000
                  and os.stat(os.path.join(root, file)).st_size > 100000]
list_10000000_size = [file.split('.')[1] for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 10000000
                  and os.stat(os.path.join(root, file)).st_size > 1000000]
out_files_dict = {
    100: (len(list_100_size), list(set(list_100_size))),
    1000: (len(list_1000_size), list(set(list_1000_size))),
    10000: (len(list_10000_size), list(set(list_10000_size))),
    100000: (len(list_100000_size), list(set(list_100000_size))),
    10000000: (len(list_10000000_size), list(set(list_10000000_size)))
}
print(out_files_dict)

with open('some_data_summary_1.json', 'w', encoding='utf-8') as f:
    json.dump(out_files_dict, f)

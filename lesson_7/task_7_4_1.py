
import os

# через цикл
out_dict = {}
list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []
list_10000000 = []
for root, dir, files in os.walk('some_data'):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 100:
            list_100.append(file)
            out_dict[100] = len(list_100)
        elif os.stat(os.path.join(root, file)).st_size <= 1000:
            list_1000.append(file)
            out_dict[1000] = len(list_1000)
        elif os.stat(os.path.join(root, file)).st_size <= 10000:
            list_10000.append(file)
            out_dict[10000] = len(list_10000)
        elif os.stat(os.path.join(root, file)).st_size <= 100000:
            list_100000.append(file)
            out_dict[100000] = len(list_100000)
        elif os.stat(os.path.join(root, file)).st_size <= 10000000:
            list_10000000.append(file)
            out_dict[10000000] = len(list_10000000)
        # else:
        #     list_1000000.append(file)
        #     out_dict[1000000] = len(list_1000000)

print(out_dict)


# через list comprehension

list_100_size = [file for root, dir, files in os.walk('some_data') for file in files
                 if os.stat(os.path.join(root, file)).st_size <= 100]
list_1000_size = [file for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 1000
                  and os.stat(os.path.join(root, file)).st_size > 100]
list_10000_size = [file for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 10000
                  and os.stat(os.path.join(root, file)).st_size > 1000]
list_100000_size = [file for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 100000
                  and os.stat(os.path.join(root, file)).st_size > 10000]
list_1000000_size = [file for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 1000000
                  and os.stat(os.path.join(root, file)).st_size > 100000]
list_10000000_size = [file for root, dir, files in os.walk('some_data')
                  for file in files if os.stat(os.path.join(root, file)).st_size <= 10000000
                  and os.stat(os.path.join(root, file)).st_size > 1000000]
out_files_dict = {
    100: len(list_100_size),
    1000: len(list_1000_size),
    10000: len(list_10000_size),
    100000: len(list_100000_size),
    10000000: len(list_10000000_size)
}
print(out_files_dict)

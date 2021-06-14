import os
import shutil
#создаем папку "--templates" в папке "--my_project"
try:
    os.mkdir('--my_project\\--templates')
except FileExistsError:
    print('Файл или папка уже существует')
except OSError as e:
    print('Возникла ошибка', e)
except Exception as e:
     print('Глобальная ошибка', e)

#ищем шаблоны, создаем аналогичные папки и копируем шаблоны в них
for root, dir, files in os.walk('--my_project'):
    for file in files:
        if file.lower().endswith('.html'):
            file_way = os.path.join(root, file)
            folder_way = os.path.dirname(file_way)
            folder_name = os.path.split(folder_way)[-1]
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}'):
                try:
                    os.mkdir(f'--my_project\\--templates\\{folder_name}')
                except OSError as e:
                    print('Возникла ошибка', e)
                except Exception as e:
                    print('Глобальная ошибка', e)
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}\\{file}'):
                try:
                    shutil.copy(file_way, f'--my_project\\--templates\\{folder_name}')
                except OSError as e:
                    print('Возникла ошибка', e)
                except Exception as e:
                    print('Глобальная ошибка', e)

# через shutil.copytree()
#создаем папку "--templates" в папке "--my_project"
try:
    os.mkdir('--my_project\\--templates')
except FileExistsError:
    print('Файл или папка уже существует')
except OSError as e:
    print('Возникла ошибка', e)
except Exception as e:
     print('Глобальная ошибка', e)

#ищем шаблоны, копируем папки с шаблонами
for root, dir, files in os.walk('--my_project'):
    for file in files:
        if file.lower().endswith('.html'):
            file_way = os.path.join(root, file)
            folder_way = os.path.dirname(file_way)
            folder_name = os.path.split(folder_way)[-1]
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}'):
                try:
                   shutil.copytree(folder_way, f'--my_project\\--templates\\{folder_name}')
                except OSError as e:
                    print('Возникла ошибка', e)
                except Exception as e:
                    print('Глобальная ошибка', e)
                    

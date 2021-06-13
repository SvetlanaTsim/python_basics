""" Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--authapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--mainhapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
 предусмотреть возможные исключительные ситуации; это реальная задача,
 которая решена, например, во фреймворке django.
"""
import os
import shutil
#создаем папку "--templates" в папке "--my_project"
if not os.path.exists('--my_project\\--templates'):
    os.mkdir('--my_project\\--templates')
#ищем шаблоны, создаем аналогичные папки и копируем шаблоны в них
for root, dir, files in os.walk('--my_project'):
    for file in files:
        if file.lower().endswith('.html'):
            file_way = os.path.join(root, file)
            folder_way = os.path.dirname(file_way)
            folder_name = os.path.split(folder_way)[-1]
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}'):
                os.mkdir(f'--my_project\\--templates\\{folder_name}')
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}\\{file}'):
                shutil.copy(file_way, f'--my_project\\--templates\\{folder_name}')

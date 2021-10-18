# #Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

config_dict = { '--my_project': ['--settings', '--authapp', '--adminapp', '--authapp']}
for dir in config_dict.keys():
    for sub_dir in config_dict[dir]:
        if not os.path.exists(f'{dir}\\{sub_dir}'):
            os.makedirs(f'{dir}\\{sub_dir}')
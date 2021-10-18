# # Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# # и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# # содержащие имена, начинающиеся с соответствующей буквы. Например:
# # >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# # {
# #     "И": ["Иван", "Илья"],
# #     "М": ["Мария"], "П": ["Петр"]
# # }
# #
# #
# # Подумайте: полезен ли будет вам оператор распаковки?
# # Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

# без сортрировки:
def thesaurus(*args):
    thesaurus_dict = {}
    for arg in args:
        thesaurus_dict[arg[0]] = [arg]

    for arg in args:
        if arg.startswith(arg[0]) and arg not in thesaurus_dict[arg[0]]:
            thesaurus_dict[arg[0]].append(arg)
    return thesaurus_dict


# с сортировкой по ключам:
def thesaurus_sort(*args):
    thesaurus_list = list(args)
    thesaurus_list.sort()
    thesaurus_dict = {}
    for name in thesaurus_list:
        thesaurus_dict[name[0]] = [name]

    for name in thesaurus_list:
        if name.startswith(name[0]) and name not in thesaurus_dict[name[0]]:
            thesaurus_dict[name[0]].append(name)
    return thesaurus_dict


# с сортировкой по ключам и .setdefault()
def thesaurus_sort_set(*args):
    thesaurus_list = list(args)
    thesaurus_list.sort()
    thesaurus_dict = {}
    for name in thesaurus_list:
        thesaurus_dict.setdefault(name[0], [])
        thesaurus_dict[name[0]].append(name)
    return thesaurus_dict


print(thesaurus('Наташа', 'Маша', 'Глаша', 'Настя', 'Петр', 'Поликарп', 'Андрей', 'Афанасий'))
print(thesaurus_sort('Наташа', 'Борис', 'Бронислав', 'Маша', 'Глаша', 'Настя', 'Петр', 'Поликарп', 'Андрей', 'Афанасий',
                     'Яна', 'Ядвига'))
print(thesaurus_sort_set('Наташа', 'Борис', 'Бронислав', 'Маша', 'Глаша', 'Настя', 'Петр', 'Поликарп', 'Андрей', 'Афанасий',
                     'Яна', 'Ядвига'))

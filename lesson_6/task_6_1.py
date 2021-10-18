# #Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
#вариант 1 через цикл
with open('nginx_logs.txt', encoding='utf-8') as f:
    log_tuple_list = []
    text = f.readlines()
    for log_string in text:
        ip_log = log_string[:log_string.find(' ')]
        request_type = log_string[log_string.find('"')+1:log_string.find(' ',log_string.find('"'))]
        requested_resource = log_string[log_string.find('/',log_string.find('"')):log_string.find('HTTP')-1]
        log_tuple = (ip_log, request_type, requested_resource)
        log_tuple_list.append(log_tuple)
print(log_tuple_list)
print(log_tuple_list[0])

#вариант 2 через генератор
with open('nginx_logs.txt', encoding='utf-8') as f:
    log_tuple_list_1 = [(log_string[:log_string.find(' ')],
                       log_string[log_string.find('"')+1:log_string.find(' ',log_string.find('"'))],
                       log_string[log_string.find('/',log_string.find('"')):log_string.find('HTTP')-1])
                      for log_string in f.readlines()]

print(log_tuple_list_1)
#выборочно посмотреть, что какие кортежи получились
print(log_tuple_list_1[0])
print(log_tuple_list_1[1])
print(log_tuple_list_1[10])

# чтобы посмотреть кортежи
for tuple in log_tuple_list_1:
    print(tuple)

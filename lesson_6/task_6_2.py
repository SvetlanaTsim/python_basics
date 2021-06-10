#*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
#Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

log_ip_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    line_sum = sum(1 for _ in f)
    f.seek(0)
    for i in range(line_sum): #51462
        log_string = f.readline()
        ip_log = log_string[:log_string.find(' ')]
        log_ip_list.append(ip_log)

ip_dict = {log_ip_list.count(ip):ip for ip in log_ip_list}
spam_request = max(ip_dict.keys())

print(f'ip спамера: {ip_dict[spam_request]},\nколичество отправленных им запросов: {spam_request}')



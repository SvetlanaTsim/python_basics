# my_dict = {'a': 4, 'b': 1, 'c': 10}
# a = max(my_dict.values())
# print(a)
# print(my_dict[a])
# print(my_dict[a])
# print(max(my_dict))
# print(my_dict.get(max(my_dict)))
# a = max(my_dict)
# print(my_dict.values(a)


# log_ip_list = []
# with open('nginx_logs.txt', encoding='utf-8') as f:
#     # count = int(sum(1 for _ in f))
#     # print(count)
#     # print(type(count))
#     for i in range(51462):
#         log_string = f.readline()
#         ip_log = log_string[:log_string.find(' ')]
#         log_ip_list.append(ip_log)
# # print(ip_log)
# # print(log_ip_list)

log_ip_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    # count = int(sum(1 for _ in f))
    # print(count)
    # print(type(count))
    line_sum = sum(1 for _ in f)
    f.seek(0)
    for i in range(line_sum): #51462
        log_string = f.readline()
        ip_log = log_string[:log_string.find(' ')]
        log_ip_list.append(ip_log)

print(log_ip_list)


# log_ip_list = []
# with open('nginx_logs.txt', encoding='utf-8') as f:
#     count = sum(1 for _ in f)
#     print(count)
#     #for i in range(count+1):
#     log_string = f.readline()
#     ip_log = log_string[:log_string.find(' ')]
#     user_ip = log_string[:log_string.find(' ')]
#     log_ip_list.append(ip_log)
# print(log_ip_list)

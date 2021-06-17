import re
parse_list = []
with open('nginx_logs.txt',encoding='utf-8') as f:
       for line in f:
              REMOTE_ADDR = re.compile(r'^[a-zA-Z.:\d]+')
              remote_addr = REMOTE_ADDR.search(line).group()
              REQUEST_DATE = re.compile(r'\d{2}[/][[a-zA-Z]+[/]\d{4}[:](?:\d{2}[:]){2}\d{2}\s[+]\d{4}')
              request_datetime = REQUEST_DATE.search(line).group()
              REQUESTED_TYPE = re.compile(r'[A-Z]{3}')
              request_type = REQUESTED_TYPE.search(line).group()
              RESOURSE = re.compile(r'(?:[/][a-z]+){2}[_]\d')
              resourse = RESOURSE.search(line).group()
              CODE_SIZE = re.compile(r'\d{3}\s\d+')
              code, size = CODE_SIZE.search(line).group().split(' ')
              result = (remote_addr, request_datetime, request_type, resourse, code, size)
              parse_list.append(result)
print(parse_list)

import re
# Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
final_list = []

for i in emails.split():
    match_find = re.search(r"(\w+)\D(\w+)[.](\D+)",i)
    if match_find:
        final_list.append(match_find.group(1,2,3))
print(final_list)

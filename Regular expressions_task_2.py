import re
#Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста.

text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better
butter, To make the bitter butter better."""

final_list = []

for i in text.split():
    match_word = re.search(r"(B|b)\w+",i)
    if match_word:
        final_list.append(match_word.group())
print(final_list)

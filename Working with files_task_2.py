#Требуется реализовать функцию longest_words(file), которая выводит
#слово, имеющее максимальную длину (или список слов, если таковых
#несколько)

def longest_word(file):
    f = open(file, encoding="utf-8")
    a = (f.read().split())
    len_word = 0
    temp_len = []

    for i in a:
        if len(i) > len_word:
            len_word = len(i)

    for i in a:
        if len(i) == len_word:
            temp_len.append(i)
    return temp_len

print(longest_word("article.txt"))


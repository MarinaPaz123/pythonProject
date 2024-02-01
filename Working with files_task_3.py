#Напишите функцию reverse(in_file, out_file), которая читает
#строки из файла in_file и создает файл out_file, куда сохраняет прочитанные
#строки в обратном порядке.

def reverse(in_file, out_file):
    with open(in_file,encoding="utf-8") as src, open(out_file,'w') as dest:
        a = src.read().split("\n")
        reversed_list = list(reversed(a))
        print(reversed_list)
        test_str = "\n".join(reversed_list)
        dest.write(test_str)

reverse("article.txt","out.txt")

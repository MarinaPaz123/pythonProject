#Даны два списка целых чисел одинаковый длины. Например [5,4,3] и [2,1,3].
#Сформировать третий список полученный путем нахождения разницы меду списками,
#например [5-2, 4-1,3-3] итоговый список [3,3,0]. Формирование третьего списка
#осуществляется с использованием функции

def func(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    return c


var = [5, 4, 3]
var1 = [2, 1, 3]

temp = func(var, var1)
print(temp)
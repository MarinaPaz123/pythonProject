# Напишите программу, которая у пользователя запрашивает две точки (верхний
# левый гол, нижний правый угол) на координатной плоскости, например (2,3), (3,5). По
# этим двум точкам строится прямоугольник.
# Подсчитать периметр прямоугольника, площадь прямоугольника.
# Далее программа запрашивает еще две точки (верхний левый угол, нижний правый угол)
# на координатной плоскости, например (1,1), (4,4) второго
# прямоугольника. Определить прямоугольники пересекаются хотя бы по одной стороне или нет.

rect1 = {"dot1":[], "dot2":[]}
rect2 = {"dot1":[], "dot2":[]}

print("Задайте размеры первого прямоугольника:")
rect1["dot1"].append(int(input("Первая точка, координата X:")))
rect1["dot1"].append(int(input("Первая точка, координата Y:")))
rect1["dot2"].append(int(input("Вторая точка, координата X:")))
rect1["dot2"].append(int(input("Вторая точка, координата Y:")))

print("\nЗадайте размеры второго прямоугольника:")
rect2["dot1"].append(int(input("Первая точка, координата X:")))
rect2["dot1"].append(int(input("Первая точка, координата Y:")))
rect2["dot2"].append(int(input("Вторая точка, координата X:")))
rect2["dot2"].append(int(input("Вторая точка, координата Y:")))

# Ищем длины сторон первого прямоугольника
rect1_side1 = rect1["dot2"][0] - rect1["dot1"][0]
rect1_side2 = rect1["dot1"][1] - rect1["dot2"][1]

print(f"Периметр первого прямоугольника: {(rect1_side1 + rect1_side2) * 2}")
print(f"Площадь первого прямоугольника: {rect1_side1 * rect1_side2}")

rect1_X = [rect1["dot1"][0], rect1["dot2"][0]]
rect1_Y = [rect1["dot1"][1], rect1["dot2"][1]]

rect2_X = [rect2["dot1"][0], rect2["dot2"][0]]
rect2_Y = [rect2["dot1"][1], rect2["dot2"][1]]

if max(rect1_X)<min(rect2_X) or max(rect1_Y) < min(rect2_Y) or min(rect1_Y) > max(rect2_Y):
    print("Прямоугольники не пересекаются")
else:
    print("Прямоугольники пересекаются")
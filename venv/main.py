# sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
# sides = sorted(sides, reverse=True)
# smax = 0
# for i in range(len(sides)):
#     for j in range(i + 1, len(sides)):
#         for k in range(j + 1, len(sides)):
#             a = sides[i]
#             b = sides[j]
#             c = sides[k]
#             if a + b > c and a + c > b and b + c > a:
#                 p = (a + b + c) / 2
#                 s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
#                 if s > smax:
#                     smax = s
# print("Максимальная площадь треугольника", smax)

import math

print("Введите 3 коэффициента квадратного уравнения: ")
a = float(input())
b = float(input())
c = float(input())
d = (b**2 - 4*a*c)
if(d<0):
    print("Нет корней")
if(d==0):
    print("Один корень: ")
    k1 = (-b + d ** (0.5))/(2*a)
    print(k1)
if(d>0):
    print("Два корня: ")
    k1 = (-b + d ** (0.5)) / (2 * a)
    print(k1)
    k2 = (-b - math.sqrt(d)) / (2*a)
    print(k2)

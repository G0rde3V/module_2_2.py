first = int(input('Введите 1-е число:'))
print(first)
second = int(input('Введите 2-е число: '))
print(second)
third = int(input('Введите 3-е число: '))
print(third)
#Если равных чисел среди 3-х вообще нет, то вывести 0
if first != second != third and second != first != third and third != first != second:
    print(0)
#Если все числа равны между собой, то вывести 3
elif first == second == third:
    print(3)
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(2)
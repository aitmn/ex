import math

#Задача 1

str1 = input()
str2 = input()
str3 = input()

print(str1 + str2 + str3)
#Ответ Программирование после школы!


#Задача 2

a = int(input())
b = int(input())

print(2**8*a**8 - 2**4*a**4 + 2**2*a**2 - 2*b + 1/2 * math.sqrt(b) + (a * b)**(b + a) / 2)
#Ответ 32134205104895.5


#Задача 3

#Ответ 23!

#Задача 4

a = int(input())
b = int(input())
c = int(input())

print('(', end='')
print(a, b, sep=' + ', end=' - ')
print(c, ') % 10', sep = '', end = ' = ')
print(((a + b - c) % 10))

#Ответ (123 + 456 - 789) % 10 = 0


#Задача 5

number = int(input())
print(number - 1, number + 1, sep='')
#Ответ 2523

#Задача 6
cm = int(input())
km = cm // 1000
print(km)

#Ответ 1234

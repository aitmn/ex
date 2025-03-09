#Задача 1
#Ответ True

#Задача 2
passwd_1 = input()
passwd_2 = input()

if passwd_2 == passwd_1:
    print(True)
else:
    print(False)

#Ответ False

#Задача 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a, b, c, d))

#Ответ 5

#Задача 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(max(a, b, c, d))

#Ответ 30

#Задача 5
a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    print(True)
else:
    print(False)

#Ответ True

#Задача 6

a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print('Равносторонний')
elif a != b and b != c and a != c:
    print('Разносторонний')
elif a + b > c and b + c > a and a + c > b:
    print('Вырожденный')

#Ответ Вырожденный

#Задача 7

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < c or d < a:
    print(0)
elif a <= c and d <= b:
    print(d - c + 1)
elif c <= a and b <= d:
    print(b - a + 1)
elif c >= a and b >= c and d >= b:
    print(b - c + 1)
elif a >= c and d >= a and d >= b:
    print(d - a + 1)

#Ответ 7
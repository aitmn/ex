
#Задача 1

n = int(input())
for i in range(0, n + 1):
    if i % 3 == 0 and i % 6 !=0:
        print(i)

#Ответ 3, 9, 15

#Задача 2

n = int(input())

for i in range(10, n + 1):
    if i % 10 % 2 == 0:
        print(i)

#Ответ 10, 12, 14, 16


#Задача 3

n = int(input())

if n % 2 == 0:
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print(count)
if n % 2 != 0:
    summa = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            summa += i
    print(summa)

#Ответ 50, 2500


#Задача 4

n = int(input())
if n % 3 == 0:
    m = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % m == 0:
            count += 1
    print(count)
if n % 3 != 0:
    for i in range(1, n + 1):
        print(n ** i, end=' ')

#Ответ 14, 8 64 512 4096 32768 262144 2097152 16777216


#Задача 5

a = int(input())
b = int(input())
n = [12, 16, 10, 20, 12, 11, 1, 19, 7, 10, 21, 22, 18]
count = 0
for i in n:
    if i > 10 and (i % 3 == 0 or i % 4 ==0):
        if a**2 + b**2 == i**2:
            count += 1
print(count)

#Ответ 1
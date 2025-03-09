#Задача 1

n = int(input())
a = [0]
for i in range(n):
    x = int(input())
    a = [i] * x
    print(a)

#Ответ [2, 2, 2]

#Задача 2

n = int(input())
a = []
for i in range(n):
    a = a + [i] * i
    print(a)

#Ответ [1, 2, 2]


#Задача 3

n = 5
lst = [2, 3, 1, 5, 10]

avg = sum(lst) / 5
print(avg)

#Ответ 4.2

#задача 4

n = 10
m = 3
lst = [1, 10, 23, 32, 18, 74,
29, 73, 1, 82]

print(lst[m])

#Ответ 32

#Задача 5

n = 6
lst = [1, 9, 2, 8, 3, 7]
summ = 0

for i in lst[::2]:
    summ += i
print(summ)

#Ответ 6
#Задача 1

x = int(input())

while x % 2 != 0 and x % 10 != 5:
    x = int(input())

#Задача 2

for i in range(10):
    print(i)

#Задача 3

k = int(input())
n = int(input())
summ = 0
while k <= n:
    if k % 2 != 0:
        summ += k
    k += 1
print(summ)
#Ответ 768182441

#Задача 4

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#Ответ 3628800
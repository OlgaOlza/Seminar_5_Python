"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
"""
a = int(input("Введите число: "))

k = 0

for el in range(2, a):
    if a % el == 0:
        k = k + 1

if k == 0:
    print("Число простое")
else:
    print("Число составное")


def recur(a, k=0, el=2):
    if el == a - 1:
        if k == 0:
            print("Число простое")
        else:
            print("Число составное")
        return

    if a % el == 0:
        k = k + 1
    return recur(a, k, el + 1)


recur(a)
"""


def is_prime(some_num):
    checker = True

    for i in range(2, some_num):
        if some_num % i == 0:
            checker = False

    return checker


print(is_prime(8))


def is_prime(some_num, checker=True, i=2):
    if i != some_num:
        if some_num % i == 0:
            checker = False

        return is_prime(some_num, checker, i + 1)
    return checker


print(is_prime(8))

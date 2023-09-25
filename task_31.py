"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1,
 ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(7))


def fibo(n):
    return n if n < 3 else fibo(n - 1) + fibo(n - 2)


print(fibo(7))


f1 = 1
f2 = 2

n = 7
n = n - 2
while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1

print(f2)

# f(6) + f(5)
#   |
# f(5) + f(4)
#   |
# f(4) + f(3)
#   |
# f(3) + f(2)
#   |
# f(2) + f(1)
#   |
# f(1)

# 8 + 5
#   |
# 5 + 3
#   |
# 3 + 2
#   |
# 2 + 1
#   |
# 1 + 1
#   |
#   1

fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
import random


def gen_ran_list(n):
    ans = [random.randint(0, 101) for _ in range(n)]
    return ans


def itx(spis, x):
    return [val for val in spis if val > x]


print("Введите длину генерируемого списа")
spis = gen_ran_list(int(input()))

print("Введите x")
x = int(input())

print(*itx(spis, x), sep=', ')

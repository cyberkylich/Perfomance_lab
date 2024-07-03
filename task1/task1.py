result = [1]
index = 0
try:
    n, m = [int(x) for x in input("Введите 2 целых числа от 1 до n через пробел ").split()]
    if n <= 0 or m <= 0:
        raise ValueError
except ValueError:
    print("Неверный ввод")
else:
    while True:
        index = (index + m - 1) % n
        if index == 0:
            break
        result.append(index + 1)
    print(*result, sep="")

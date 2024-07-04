import sys


def main():
    try:
        n, m = [int(x) for x in sys.argv[1:3]]
        if n <= 0 or m <= 0:
            raise ValueError
    except ValueError:
        print("Неверный ввод. Убедитесь, что вы ввели два целых числа больше нуля.")
        return

    result = [1]
    index = 0

    while True:
        index = (index + m - 1) % n
        if index == 0:
            break
        result.append(index + 1)

    print(*result, sep="")


if __name__ == "__main__":
    main()

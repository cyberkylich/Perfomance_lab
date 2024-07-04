import sys


def main():
    try:
        circle_file = sys.argv[1]
        dots_file = sys.argv[2]
    except IndexError:
        print("Укажите два файла в качестве аргументов командной строки")
        return

    try:
        with open(circle_file) as circle:
            x_circle, y_circle = [float(x) for x in circle.readline().split(" ")]
            r_circle = float(circle.readline()) ** 2
    except ValueError:
        print(f"В файле {circle_file} ошибка ValueError")
        return
    except FileNotFoundError:
        print(f"Файл {circle_file} не найден")
        return

    try:
        with open(dots_file) as dots:
            for i in dots.readlines():
                try:
                    xy_dots = [float(x) for x in i.split(" ")]
                except ValueError:
                    print(f"В файле {dots_file} ошибка ValueError")
                    continue

                hypotenuse = (xy_dots[0] - x_circle) ** 2 + (xy_dots[1] - y_circle) ** 2
                if hypotenuse > r_circle:
                    print(2)
                elif hypotenuse == r_circle:
                    print(0)
                else:
                    print(1)
    except FileNotFoundError:
        print(f"Файл {dots_file} не найден")


if __name__ == "__main__":
    main()

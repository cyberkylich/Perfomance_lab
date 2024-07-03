circle = open("1.txt")
dots = open("2.txt")

try:
    x_circle, y_circle = [float(x) for x in circle.readline().split(" ")]
    r_circle = float(circle.readline()) ** 2
except ValueError:
    print("В файле 1.txt ошибка ValueError")
else:
    for i in dots.readlines():
        try:
            xy_dots = [float(x) for x in i.split(" ")]
        except ValueError:
            print("В файле 2.txt ошибка ValueError")
            continue

        hypotenuse = (xy_dots[0] - x_circle) ** 2 + (xy_dots[1] - y_circle) ** 2
        if hypotenuse > r_circle:
            print(2)
        elif hypotenuse == r_circle:
            print(0)
        else:
            print(1)
finally:
    circle.close()
    dots.close()

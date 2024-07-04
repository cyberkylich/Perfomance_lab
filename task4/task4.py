import sys


def read_file(file_path):
    try:
        with open(file_path) as file:
            array = [int(x) for x in file]
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
    return array


def moves(array):
    array.sort()
    if len(array) % 2 != 0:
        m = int((len(array) + 1) / 2 - 1)
        median = array[m]
    else:
        m1 = int(len(array) / 2 - 1)
        m2 = int(len(array) / 2)
        median = (array[m1] + array[m2]) / 2
    min_moves = sum(abs(item - median) for item in array)
    return int(min_moves)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите путь до файла")
        sys.exit(1)
    file_path = sys.argv[1]
    array = read_file(file_path)
    print(moves(array))

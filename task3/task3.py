import json
import sys


def read_files(values_path, tests_path):
    try:
        with open(values_path) as file:
            values_data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {values_path} не найден")
    try:
        with open(tests_path) as file:
            tests_data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {tests_path} не найден")
    return values_data, tests_data


def update_values(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        else:
            test['value'] = None
        if 'values' in test:
            update_values(test['values'])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Укажите три файла в качестве аргументов командной строки. Первый аргумент - values.json, второй - "
            "tests.json, третий - куда сохранить результат report.json")
        sys.exit(1)
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    values_data, tests_data = read_files(values_path, tests_path)
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    update_values(tests_data['tests'])
    with open(report_path, 'w') as file:
        json.dump(tests_data, file, indent=2)
    print(f"Результат сохранен по пути {report_path}")

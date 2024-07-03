import json


def read_files(values_path, tests_path):
    try:
        with open(values_path, 'r') as file:
            values_data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {values_path} не найден")
    try:
        with open(tests_path, 'r') as file:
            tests_data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {tests_path} не найден")
    else:
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
    values_path = input("Введите путь до values.json ")
    tests_path = input("Введите путь до tests.json ")
    report_path = input("Введите путь куда сохранить файл report.json ")
    values_data, tests_data = read_files(values_path, tests_path)
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    update_values(tests_data['tests'])
    with open(report_path, 'w') as file:
        json.dump(tests_data, file, indent=2)
    print(f"Результат сохранен по пути {report_path}")

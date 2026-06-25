from officials import Ministry

def parse_number(s):
    try:
        return float(s)
    except ValueError:
        return None

def load_from_file(filename):
    ministry = Ministry()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return None

    lines = [line.strip() for line in lines if line.strip()]
    if not lines:
        print("Ошибка: файл пуст.")
        return None

    try:
        n = int(lines[0])
    except ValueError:
        print("Ошибка: первая строка должна содержать целое число.")
        return None

    if len(lines) - 1 != n:
        print(f"Ошибка: ожидалось {n} записей, получено {len(lines) - 1}.")
        return None

    for i in range(1, n + 1):
        parts = lines[i].split()
        if len(parts) != 3:
            print(f"Ошибка в строке {i}: требуется 3 поля.")
            return None
        name = parts[0]
        bribe_str = parts[1]
        bribe = parse_number(bribe_str)
        if bribe is None:
            print(f"Ошибка: взятка для {name} должна быть числом.")
            return None
        if bribe < 0:
            print(f"Ошибка: взятка для {name} отрицательная.")
            return None
        boss = parts[2]
        try:
            ministry.add_official(name, bribe, boss)
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None

    try:
        ministry.build_tree()
    except ValueError as e:
        print(f"Ошибка при построении иерархии: {e}")
        return None

    if ministry.root is None:
        print("Ошибка: не найден главный чиновник (начальник '0').")
        return None

    return ministry
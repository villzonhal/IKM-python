from officials import Ministry
from file_loader import load_from_file

def parse_number(s):
    try:
        return float(s)
    except ValueError:
        return None

def input_manually():
    ministry = Ministry()
    
    while True:
        n_input = input("Введите количество чиновников (или 'назад' для выхода в меню): ").strip()
        if n_input.lower() == "назад":
            return None
        try:
            n = int(n_input)
            break
        except ValueError:
            print("Ошибка: требуется целое число. Попробуйте снова.")
            continue
    
    for i in range(1, n + 1):
        while True:
            line = input(f"Чиновник {i} (Введи его имя, сумму взятки, его начальника) или 'назад' для выхода: ").strip()
            if line.lower() == "назад":
                return None
            
            parts = line.split()
            if len(parts) != 3:
                print("Ошибка: строка должна содержать 3 поля (ИМЯ ВЗЯТКА НАЧАЛЬНИК). Попробуйте снова.")
                continue
            
            name = parts[0]
            bribe_str = parts[1]
            bribe = parse_number(bribe_str)
            if bribe is None:
                print(f"Ошибка: взятка для {name} должна быть числом. Попробуйте снова.")
                continue
            if bribe < 0:
                print(f"Ошибка: взятка для {name} отрицательная. Попробуйте снова.")
                continue
            boss = parts[2]
            
            try:
                ministry.add_official(name, bribe, boss)
                break
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте снова.")
                continue

    try:
        ministry.build_tree()
    except ValueError as e:
        print(f"Ошибка при построении иерархии: {e}")
        return None

    if ministry.root is None:
        print("Ошибка: не найден главный чиновник (начальник '0').")
        return None

    return ministry

def main():
    ministry = None
    running = True
    while running:
        print("\n--- МЕНЮ (ЧИНОВНИКИ) ---")
        print("1. Загрузить данные из файла")
        print("2. Ввести данные вручную")
        print("3. Решить задачу")
        print("4. Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            while True:
                filename = input("Введите имя файла (или 'назад' для выхода в меню): ").strip()
                if filename.lower() == "назад":
                    break
                if not filename:
                    print("Имя файла не может быть пустым. Попробуйте снова.")
                    continue
                ministry = load_from_file(filename)
                if ministry is not None:
                    print("Данные загружены.")
                    print(f"Всего чиновников: {len(ministry.officials)}")
                    print(f"Главный: {ministry.root.name}")
                    break
                else:
                    print("Загрузка не удалась. Попробуйте снова или введите 'назад'.")
                    continue

        elif choice == "2":
            ministry = input_manually()
            if ministry is not None:
                print("Данные введены.")
                print(f"Всего чиновников: {len(ministry.officials)}")
                print(f"Главный: {ministry.root.name}")
            else:
                print("Ввод данных отменён.")

        elif choice == "3":
            if ministry is None:
                print("Сначала загрузите или введите данные.")
            else:
                try:
                    total_money, order = ministry.solve()
                    print("\nРезультат:")
                    print(f"Минимальная сумма взяток: {total_money} у.е.")
                    print("Порядок получения подписей (снизу вверх):")
                    print(" -> ".join(order))
                except ValueError as e:
                    print(f"Ошибка: {e}")

        elif choice == "4":
            print("Выход.")
            running = False

        else:
            print("Неверный пункт. Введите 1, 2, 3 или 4.")

        if running:
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
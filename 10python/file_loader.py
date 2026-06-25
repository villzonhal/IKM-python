from queue_logic import Queue
from queue_processor import process_command

def load_from_file(filename):
    queue = Queue()
    results = []
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return None
    except PermissionError:
        print("Ошибка: нет доступа к файлу.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

    if not lines:
        print("Ошибка: файл пуст.")
        return None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        result, should_exit = process_command(queue, line)
        results.append(result)
        if should_exit:
            break
    
    return results
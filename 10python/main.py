from queue_logic import Queue
from queue_processor import process_command
from file_loader import load_from_file

def interactive_mode():
    queue = Queue()
    print("\n" + "="*60)
    print("  РЕЖИМ ИНТЕРАКТИВНОГО ВВОДА КОМАНД")
    print("="*60)
    print("ДОСТУПНЫЕ КОМАНДЫ:")
    print("  push <число>   - добавить число в конец очереди")
    print("  pop            - удалить и вывести первый элемент")
    print("  front          - показать первый элемент без удаления")
    print("  show           - показать всю очередь")
    print("  size           - показать количество элементов")
    print("  clear          - очистить очередь")
    print("  exit           - завершить работу")
    print("  назад          - вернуться в главное меню")
    print("="*60)
    
    while True:
        command = input("\n> ").strip()
        
        # Обработка команды "назад" (регистронезависимо)
        if command.lower() == "назад":
            print("Возврат в меню.")
            break
        
        if not command:
            continue
        
        result, should_exit = process_command(queue, command)
        print(result)
        
        if should_exit:
            break

def file_mode():
    while True:
        filename = input("  Введите имя файла (или 'назад' для выхода в меню): ").strip()
        if filename.lower() == "назад":
            return
        if not filename:
            print("  Ошибка: имя файла не может быть пустым. Попробуйте снова.")
            continue
        
        results = load_from_file(filename)
        if results is None:
            print("  Загрузка не удалась. Попробуйте снова или введите 'назад'.")
            continue
        
        print("\n" + "="*60)
        print("  РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ КОМАНД ИЗ ФАЙЛА")
        print("="*60)
        for result in results:
            print(result)
        print("="*60)
        break

def main():
    while True:
        print("\n" + "="*60)
        print("  ОЧЕРЕДЬ")
        print("="*60)
        print("  1. Интерактивный режим (ввод команд вручную)")
        print("  2. Загрузить команды из файла")
        print("  3. Выход")
        print("="*60)
        choice = input("  Ваш выбор: ").strip()

        if choice == "1":
            interactive_mode()
        
        elif choice == "2":
            file_mode()
        
        elif choice == "3":
            print("\n  Выход.")
            break
        
        else:
            print("  Ошибка: неверный пункт. Введите 1, 2 или 3.")
        
        if choice != "3":
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
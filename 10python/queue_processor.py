from queue_logic import Queue

def parse_number(s):
    try:
        return float(s)
    except ValueError:
        return None

def process_command(queue, command_line):
    parts = command_line.strip().split()
    if not parts:
        return "error: пустая команда", False

    cmd = parts[0].lower()
    
    if cmd == "push":
        if len(parts) != 2:
            return "error: команда push требует число (пример: push 5)", False
        n = parse_number(parts[1])
        if n is None:
            return "error: аргумент должен быть числом", False
        return queue.push(n), False
    
    elif cmd == "pop":
        return queue.pop(), False
    
    elif cmd == "front":
        return queue.front(), False
    
    elif cmd == "size":
        return queue.size(), False
    
    elif cmd == "clear":
        return queue.clear(), False
    
    elif cmd == "show":
        return queue.show(), False
    
    elif cmd == "exit":
        return queue.exit(), True
    
    else:
        return f"error: неизвестная команда '{parts[0]}'", False
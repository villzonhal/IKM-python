class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return "ok"

    def pop(self):
        if not self.items:
            return "error: очередь пуста"
        return str(self.items.pop(0))

    def front(self):
        if not self.items:
            return "error: очередь пуста"
        return str(self.items[0])

    def size(self):
        return str(len(self.items))

    def clear(self):
        self.items = []
        return "ok"

    def show(self):
        if not self.items:
            return "очередь пуста"
        return " -> ".join(str(x) for x in self.items)

    def exit(self):
        return "bye"
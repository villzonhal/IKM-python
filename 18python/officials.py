class Official:
    def __init__(self, name, bribe, boss):
        self.name = name
        self.bribe = bribe
        self.boss = boss
        self.children = []

class Ministry:
    def __init__(self):
        self.officials = {}
        self.root = None
        self.root_found = False

    def add_official(self, name, bribe, boss):
        if bribe < 0:
            raise ValueError(f"Взятка для {name} не может быть отрицательной")
        official = Official(name, bribe, boss)
        self.officials[name] = official
        if boss == "0":
            if self.root_found:
                raise ValueError(f"Обнаружено несколько главных чиновников: {name}")
            self.root = official
            self.root_found = True

    def build_tree(self):
        for official in self.officials.values():
            if official.boss != "0":
                boss_obj = self.officials.get(official.boss)
                if boss_obj is None:
                    raise ValueError(f"Начальник {official.boss} чиновника {official.name} не найден")
                boss_obj.children.append(official)

    def _find_min_path(self, node):
        if not node.children:
            return node.bribe, [node.name]
        best_cost = float("inf")
        best_path = []
        for child in node.children:
            cost, path = self._find_min_path(child)
            if cost < best_cost:
                best_cost = cost
                best_path = path
        return node.bribe + best_cost, [node.name] + best_path

    def solve(self):
        if self.root is None:
            raise ValueError("Главный чиновник не задан")
        total_cost, path_from_root = self._find_min_path(self.root)
        return total_cost, list(reversed(path_from_root))
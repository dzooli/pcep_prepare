from typing import List


class Stack:
    def __init__(self):
        self._items : List = []

    def empty(self) -> bool:
        try:
            return len(self._items) == 0
        except TypeError:
            return True

    def __len__(self):
        if not self.empty():
            return len(self._items)
        else:
            return 0

    def top(self):
        if not self.empty():
            return self._items[-1]

    def bottom(self):
        if not self.empty():
            return self._items[0]

    def push(self, item) -> bool:
        try:
            self._items.append(item)
        except MemoryError:
            return False
        return True

    def pop(self):
        if not self.empty():
            result = self._items[-1]
            del self._items[-1]
            return result
        return None

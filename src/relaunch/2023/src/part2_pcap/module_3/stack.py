from typing import List


class Stack:
    def __init__(self):
        self._items : List = list()

    def empty(self) -> bool:
        return self._items and len(self._items) > 0

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

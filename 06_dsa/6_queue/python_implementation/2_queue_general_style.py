
# importing dequeue from collection
from collections import deque
from typing import Optional, Any, Iterable

class Queue:
    def __init__(
            self,
            iterable: Optional[list[int]] = None,
            maxlen: Optional[int] = None,
    ) -> None:
        self._deque = deque(iterable if iterable is not None else [], maxlen=maxlen)
        self._maxlen = maxlen

    def push_front(self, item: Any):
        self._deque.appendleft(item)

    def push_back(self, item: Any):
        self._deque.append(item)

    def is_empty(self):
        return len(self._deque) == 0

    def pop_front(self):
        if self.is_empty():
            return None

        return self._deque.popleft()

    def pop_back(self):
        if self.is_empty():
            return None

        return self._deque.pop()

    def peek_front(self):
        if self.is_empty():
            return None

        return self._deque[0]

    def peek_back(self):
        if self.is_empty():
            return None

        return self._deque[-1]

    def size(self):
        return len(self._deque)

    def clear(self):
        if self.is_empty():
            return None

        self._deque.clear()

    def contains(self, item: Any) -> bool:
        if self.is_empty():
            return False

        return item in self._deque

    def index(self, item: Any, start: int = 0, end: Optional[int] = None) -> int:
        

# 225: Implement Stack using Queues

from collections import deque 

class MyStack:
    def __init__(self):
        self.q = deque([])
        self.size = 0
        
    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1
        
    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        self.size -= 1
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if self.size == 0: return True
        return False
        



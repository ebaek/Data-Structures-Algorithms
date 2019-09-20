# 232: Implement Queue using Stacks

class MyQueue:
    def __init__(self):
        self.stack = []
        self.stackQueue = []

    def push(self, x: int) -> None:
        self.stack.push(x)
        
    def pop(self) -> int:
        while len(self.stack) > 0:
            self.stackQueue.append(self.stack.pop())
        
        popped = self.stackQueue.pop()

        while len(self.stackQueue) > 0:
            self.stack.append(self.stackQueue.pop())
        
        return popped

    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        if len(self.stack) == 0: return true
        return false
        

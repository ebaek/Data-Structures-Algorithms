# 146: LRU Cache

class ListNode:
    def __init__(self, val):
        self.val = val
        self.key = None
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.dict = {}
        
        self.capacity = capacity 
        self.currCap = 0

    def get(self, key: int) -> int:
        if key in self.dict: 
            self.deleteNode(self.dict[key])
            self.moveToHead(self.dict[key])
            return self.dict[key].val
        else: return -1
    
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node 
    
    def deleteNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def moveToHead(self, node):
        self.deleteNode(node)
        self.addNode(node)
        
    def removeFromTail(self):
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        del self.dict[last.key]
        self.currCap -= 1
               
    def put(self, key: int, value: int) -> None:
        node = None
        
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.deleteNode(node)
        else:
            node = ListNode(value)
            node.key = key
            self.currCap += 1
        
        self.dict[key] = node
        self.addNode(node)
        
        if self.currCap > self.capacity:
            self.removeFromTail()

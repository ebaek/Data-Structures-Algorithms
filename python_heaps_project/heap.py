class MinHeap:
    def __init__(self):
        self.arrNodes = [None]
        
    def getParentIdx(self, nodeIdx):
        return nodeIdx // 2

    def getLeftChildIdx(self, nodeIdx):
        return nodeIdx*2
    
    def getRightChildIdx(self, nodeIdx):
        return nodeIdx*2 + 1
    
    def siftUp(self, idx):
        if idx == 1: return
        
        parentIdx = self.getParentIdx(idx)
        
        if self.arrNodes[idx] < self.arrNodes[parentIdx]:
            self.arrNodes[idx], self.arrNodes[parentIdx] = self.arrNodes[parentIdx], self.arrNodes[idx]
            self.siftUp(parentIdx)
    
    def insert(self, val):
        self.arrNodes.append(val)
        self.siftUp(len(self.arrNodes)-1)
    
    def deleteMin(self):
        if len(self.arrNodes) == 1: return None
        if len(self.arrNodes) == 2: return self.arrNodes.pop()
        
        minNode = self.arrNodes[1]
        self.arrNodes[1] = self.arrNodes.pop()
        self.siftDown(1)
        return minNode
    
    def siftDown(self, idx):
        leftChildIdx = self.getLeftChildIdx(idx) if self.getLeftChildIdx(idx) < len(self.arrNodes) else 0
        rightChildIdx = self.getRightChildIdx(idx) if self.getRightChildIdx(idx) < len(self.arrNodes) else 0

        leftVal = self.arrNodes[leftChildIdx]
        rightVal = self.arrNodes[rightChildIdx]
        
        if (not leftVal or self.arrNodes[idx] < leftVal) and (not rightVal or self.arrNodes[idx] < rightVal): return
        
        swapIdx = None
        
        if leftVal < rightVal:
            swapIdx = leftChildIdx
        else:
            swapIdx = rightChildIdx
            
        self.arrNodes[idx], self.arrNodes[swapIdx] = self.arrNodes[swapIdx], self.arrNodes[idx]
        self.siftDown(swapIdx)
        
        
a = MinHeap()
a.insert(23423)
a.insert(-4344)
a.insert(2)
a.insert(3)
a.insert(4)
print(a.arrNodes)
print(a.deleteMin())
print(a.deleteMin())
print(a.deleteMin())
print(a.arrNodes)

        
        
        
        
        
        
        
    
    

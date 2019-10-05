# 346: Moving Average from Data Stream

# naive approach, but can use a deque to remove and add items 
# when the length of the window has been met 

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.history = []
        self.start = 0
        
    def next(self, val: int) -> float:
        sum = 0
        self.history.append(val)
        
        if len(self.history) == 1:
            return val
        elif 2 < len(self.history) <= self.size:
            for el in self.history:
                sum += el
            return sum / len(self.history)
        else:
            self.start += 1
            end = self.start + self.size
            
            for idx in range(self.start, end):
                sum += self.history[idx]
    
            return sum / self.size 

# faster approach, more efficient eliminates need for recalculation
class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.currTotal = 0
        self.currIdx = 0
        self.size = size

    def next(self, val: int) -> float:
        self.arr.append(val)
        if len(self.arr) == 1:
            self.currTotal += val
            return self.arr[0]
        elif len(self.arr) <= self.size:
            self.currTotal += val
            return (self.currTotal) / len(self.arr)
        else:
            self.currTotal += (val - self.arr[self.currIdx])
            self.currIdx += 1
            return self.currTotal / self.size

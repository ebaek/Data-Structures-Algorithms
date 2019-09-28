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

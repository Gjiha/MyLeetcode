class RLEIterator:

    def __init__(self, encoding: list[int]):
        
        self.list = encoding 
        self.index = 0


    def next(self, n: int) -> int:

        i = self.index

        iteration = n

        while i < len(self.list):

            if (self.list[i] - iteration) > 0:
                self.list[i] -= iteration
                return self.list[i + 1]
            
            elif (self.list[i] - iteration) < 0: 
                iteration -= self.list[i]
                self.index += 2
                i += 2

            else:
                self.list[i] -= iteration
                self.index += 2
                return self.list[i + 1]
            
        return -1

R = RLEIterator([3,8,0,9,2,5])
print(R.next(2))
print(R.next(1))
print(R.next(1))
print(R.next(2))


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
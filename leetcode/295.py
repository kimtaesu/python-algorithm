class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        n = len(self.list)
        if n == 1:
            return self.list[-1]
        elif n < 3:
            return sum(self.list) * 0.5
        if n % 2 == 0:
            mid = int(len(self.list) / 2)
            x = self.list[mid - 1]
            x2 = self.list[mid]
            return x + x2 / 2
        else:
            mid = int(len(self.list) / 2)
            return self.list[mid]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
print(obj.findMedian())

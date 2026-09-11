import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        #if value is greater than element at 
        #root of min heap, add to max heap
        #if the absolute diff of the heaps is > 1
        #pop from larger and add to smaller heap

        

        if self.min_heap and num > self.min_heap[0]: #add to max heap
            heapq.heappush(self.min_heap, num)
        else: #add to min
            heapq.heappush(self.max_heap, -num)

        #check if len diff is > 1
        if len(self.min_heap) - len(self.max_heap) > 1: #remove from min
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        elif len(self.max_heap) - len(self.min_heap) > 1: #remove from max
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val) 

    def findMedian(self) -> float:
        if len(self.min_heap) - len(self.max_heap) == 1:
            return self.min_heap[0]
        elif len(self.max_heap) - len(self.min_heap) == 1:
            return -self.max_heap[0]
        else:
            return ((-self.max_heap[0]) + self.min_heap[0]) / 2

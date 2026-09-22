import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        passengers = 0

        trips.sort(key=lambda x: x[1])

        for num_passengers, start, end in trips:

            while heap and heap[0][0] <= start:
                _, pop = heapq.heappop(heap)
                passengers -= pop



            passengers += num_passengers
            if passengers > capacity:
                return False

            heapq.heappush(heap, (end, num_passengers))
            


        return True
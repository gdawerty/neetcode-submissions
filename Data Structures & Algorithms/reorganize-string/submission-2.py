class Solution:
    def reorganizeString(self, s: str) -> str:

        freq= defaultdict(int)

        for char in s:
            freq[char] += 1

        heap = []

        for key, value in freq.items():
            if value > (len(s) + 1) // 2:
                return ""
            heap.append((-value, key))


        heapq.heapify(heap)

        new_s = []

        prev = None

        while heap:
            cnt, key = heapq.heappop(heap)


            new_s.append(key)

            if prev:
                heapq.heappush(heap, prev)

            if cnt + 1 < 0:
                prev = (cnt + 1, key)
            else:
                prev = None

        return "".join(new_s)
            



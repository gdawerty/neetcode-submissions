class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1

        counts_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        lists = []
        for i in range(k):
            lists.append(counts_sorted[i][0])
        
        return lists
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] +=1

        arr = []

        for num, val in counts.items():
            arr.append([val, num])

        arr = sorted(arr)
        print(arr)
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res
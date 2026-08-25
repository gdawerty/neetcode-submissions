
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        di = defaultdict(int)

        for num in nums:
            di[num] +=1



        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in di.items():
            buckets[val].append(key)

        res = []
        end = len(buckets) - 1
        while k > 0:
            if buckets[end]:
                for num in buckets[end]:
                    res.append(num)
                    k-=1
                    if k == 0:
                        return res
            end-=1
        return res

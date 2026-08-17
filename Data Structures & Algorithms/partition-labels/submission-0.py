class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        counts = {}

        for index, char in enumerate(s):
            counts[char] = index


        start = end = 0

        for i, val in enumerate(s):
            end = max(end, counts[val])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        
        return res



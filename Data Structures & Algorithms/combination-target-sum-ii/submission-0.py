class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        def backtrack(index, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            if remaining < 0 or index == len(candidates):
                return

            path.append(candidates[index])
            backtrack(index + 1, remaining - candidates[index], path)
            path.pop()

            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index +=1
            backtrack(index + 1, remaining, path)

        res = []

        backtrack(0, target, [])
        return res
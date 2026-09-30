class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def backtrack(idx, total, curr):
            if total == target:
                
                res.append(curr.copy())
                return

            elif idx == len(candidates) or total > target:
                return

            curr.append(candidates[idx])
            backtrack(idx + 1, total + candidates[idx], curr)
            curr.pop()

            next_idx = idx + 1

            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            backtrack(next_idx, total, curr)

        backtrack(0, 0, [])

        return res
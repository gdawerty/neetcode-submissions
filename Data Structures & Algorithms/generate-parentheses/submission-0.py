class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                res.append(path)
                return

            if open_count < n:
                path1 = path + "("
                backtrack(path1, open_count + 1, close_count)

            if close_count < open_count:
                path2 = path + ")"
                backtrack(path2, open_count, close_count + 1)


        backtrack("", 0, 0)
        return res
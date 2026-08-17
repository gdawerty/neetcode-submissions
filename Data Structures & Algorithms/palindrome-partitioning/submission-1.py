class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            l = 0
            r = len(substring) - 1

            while l < r:
                if substring[l] != substring[r]:
                    return False
                l+=1
                r-=1

            return True

        def backtrack(start_index, path):
            if start_index == len(s):
                res.append(path[:])
                return

            for end in range(start_index, len(s)):
                substring = s[start_index:end+1]
                if is_palindrome(substring):
                    # choose
                    path.append(substring)
                    backtrack(end + 1, path)
                    # un-choose
                    path.pop()



        res = []
        backtrack(0, [])

        return res
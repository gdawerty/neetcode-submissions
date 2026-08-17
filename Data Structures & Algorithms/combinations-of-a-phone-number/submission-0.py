class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            if index == len(digits):
                return

            curr = digits[index]
            for char in digitToChar[curr]:
                
                backtrack(index + 1, path + char)

        if digits:
            backtrack(0, '')

        return res
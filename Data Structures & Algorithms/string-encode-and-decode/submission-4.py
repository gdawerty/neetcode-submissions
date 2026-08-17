class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for string in strs:
            s = s + string
            s = s + "."

        return s

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""

        for char in s:
            if char != ".":
                word+=char
            else:
                res.append(word)
                word = ""

        return res
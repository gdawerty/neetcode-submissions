class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for word in strs:
            output += word
            output += "."

        print(output)
        return output

    def decode(self, s: str) -> List[str]:

        strs = []
        mark = 0
        for i in range (len(s)):
            if s[i] == ".":
                strs.append(s[mark:i])
                mark = i + 1
        return strs
        
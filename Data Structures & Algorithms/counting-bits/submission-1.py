class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(len(res)):
            temp = i
            while temp > 0:
                if temp & 1 == 1:
                    res[i] +=1
                temp = temp >> 1


        return res
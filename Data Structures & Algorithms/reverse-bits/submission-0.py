class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            is_one = (n >> i) & 1
            res += is_one << (31 - i)

        return res
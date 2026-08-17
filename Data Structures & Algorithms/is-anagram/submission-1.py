class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}

        for char_s in s:
            if char_s not in set_s:
                set_s[char_s] = 1
            else:
                set_s[char_s] += 1

        set_t = {}

        for char_t in t:
            if char_t not in set_t:
                set_t[char_t] = 1
            else:
                set_t[char_t] += 1

        return set_s == set_t
    



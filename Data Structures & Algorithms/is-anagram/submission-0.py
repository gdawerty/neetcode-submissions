class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hash_table_s = {}
        hash_table_t = {}

        for char in s:
            if char in hash_table_s:
                # If we've seen this char before, increase its count
                hash_table_s[char] += 1
            else:
                # If this is the first time seeing the char, set count to 1
                hash_table_s[char] = 1
        
        for char in t:
            hash_table_t[char] = hash_table_t.get(char, 0) + 1
        
        return hash_table_s == hash_table_t

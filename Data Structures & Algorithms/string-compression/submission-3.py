class Solution:
    def compress(self, chars: List[str]) -> int:
        # idea is to get the compressed string
        #then get len of it
        #then modify the current list with the first k elements

        n = len(chars)
        i = 0
        k = 0

        while i < n:
            chars[k] = chars[i]
            k+=1
            j = i + 1

            while j < n and chars[i] == chars[j]:
                j+=1
            
            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k+=1
            i = j
        return k
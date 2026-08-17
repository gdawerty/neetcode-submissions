class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        def palindrome(left, right):
            curr = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curr+=1
                    left-=1
                    right+=1
                else:
                    break

            return curr



        for i in range(len(s)):
            count += palindrome(i, i)
            count += palindrome(i, i + 1)

        return count
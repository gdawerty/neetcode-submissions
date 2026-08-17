class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res_start = 0
        res_end = 0

        def palindrome(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -=1
                    right +=1
                else:
                    break
            
            return left + 1, right -1

        
        for i in range(len(s)):
            l1, r1 = palindrome(i, i)
            l2, r2 = palindrome(i, i + 1)

            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1



            if len1 >= len2:
                cur_len = len1
                cur_l, cur_r = l1, r1
            else:
                cur_len = len2
                cur_l, cur_r = l2, r2


            if cur_len > res_end:
                res_start = cur_l
                res_end = cur_len


        return s[res_start: res_start + res_end]
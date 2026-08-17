from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #loop thru the list, get frequency of letters
        count = defaultdict(list)

        for word in strs:
            res1 = [0] * 26
            for char in word:
                num = ord(char) - ord('a')
                res1[num] +=1

            count[tuple(res1)].append(word)
            

        return list(count.values())


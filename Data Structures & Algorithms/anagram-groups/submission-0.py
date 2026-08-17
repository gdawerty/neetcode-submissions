class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result = list(groups.values())
        return result
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.endOfWord

            ch = word[index]

            if ch == ".":
                for child in node.children:
                    if child and dfs(index + 1, child):
                        return True
                return False
            else:
                child = node.children[ord(ch) - ord('a')]

                if not child:
                    return False
                else:
                    return dfs(index + 1, child)

        return dfs(0, self.root)


        

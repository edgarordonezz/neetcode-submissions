class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            # if letter not in word, add to the path
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool: 
        
        def dfs(curr, j):
            if j == len(word):
                return curr.end
            c = word[j]
            if c == ".":
                for child in curr.children.values():
                    if dfs(child, j + 1):
                        return True
                return False
            else:
                # normal letter case
                if c not in curr.children:
                    return False
                return dfs(curr.children[c], j+1)
        return dfs(self, 0)
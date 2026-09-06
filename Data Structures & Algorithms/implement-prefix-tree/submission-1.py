class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end = False # mark when a word ends

    def insert(self, word: str) -> None:
        curr = self
        # for every letter, if it doesnt exist create a new PrefixTree
        # if it does exist, keep traversing down children
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixTree()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        # for every letter, if it doesnt exist return False early
        # search and if curr.end is False it means it hasnt ended
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
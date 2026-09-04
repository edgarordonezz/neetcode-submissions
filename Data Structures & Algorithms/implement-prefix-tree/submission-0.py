class PrefixTree:
    

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            # if letter is not in the current path 
            if char not in curr.children:
                curr.children[char] = PrefixTree()
            # make new node the current position
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            # if letter not in current path
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
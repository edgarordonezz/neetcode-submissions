class PrefixTree:

    def __init__(self):
        # root, this is where words begin
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                # if w not in children dict, create a new node for w
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return True
                
            
    
class TrieNode:

    def __init__(self):

        self.children = {}
        self.end = False
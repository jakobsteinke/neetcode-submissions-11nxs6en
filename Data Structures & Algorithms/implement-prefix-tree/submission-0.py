class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        if not word:
            return
        if word[0] not in self.children:
            self.children[word[0]] = PrefixTree()
        self.children[word[0]].insert(word[1:])
        if len(word) == 1:
            self.children[word[0]].is_word = True


    def search(self, word: str) -> bool:
        if not word:
            return True
        if word[0] not in self.children:
            return False
        if len(word) == 1:
            return self.children[word[0]].is_word
        return self.children[word[0]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] not in self.children:
            return False
        return self.children[prefix[0]].startsWith(prefix[1:])
        
        
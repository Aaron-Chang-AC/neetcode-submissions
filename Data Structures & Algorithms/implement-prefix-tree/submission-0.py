class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        word += "@"
        cur = self.tree
        i = 0
        while i < len(word):
            if word[i] not in cur:
                cur[word[i]] = {}
            cur = cur[word[i]]
            i+=1
        # print(self.tree)

    def search(self, word: str) -> bool:
        word += "@"
        cur = self.tree
        i = 0
        while i < len(word):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
            i+=1
        if len(cur) == 0:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree
        i = 0
        while i < len(prefix):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
            i+=1
        return True
        
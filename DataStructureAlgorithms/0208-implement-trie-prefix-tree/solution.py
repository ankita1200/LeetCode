class Trie:

    def __init__(self):
        self.data = set()
        self.prefs = set()

    def insert(self, word: str) -> None:
        cur = ''
        for char in word:
            cur += char
            self.prefs.add(cur)
        self.data.add(word)

    def search(self, word: str) -> bool:
        return word in self.data

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefs

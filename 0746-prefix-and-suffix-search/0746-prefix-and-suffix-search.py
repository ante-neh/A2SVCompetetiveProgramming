Trie = lambda: collections.defaultdict(Trie)
wei = False
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i,word in enumerate(words):
            word += '#'
            for tmp in range(len(word)):
                cur = self.trie
                cur[wei] = i
                for j in range(tmp,2*len(word) - 1):
                    cur = cur[word[j%len(word)]]
                    cur[wei] = i
    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for combi in suffix + '#' + prefix:
            if combi not in cur:
                return -1
            cur = cur[combi]
        return cur[wei]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
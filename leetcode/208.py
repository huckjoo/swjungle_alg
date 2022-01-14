class Trie:
    def __init__(self):
        self.link = {}

    def insert(self, word):
        t = self.link
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'  # 마지막 노드라는 표시

    def search(self, word):
        t = self.link
        for w in word:
            if w not in t:  # dcron을 찾다가 c가 없으면 바로 False return
                return False
            t = t[w]
        # 왜 if t['#'] == '#': return True를 하면 안될까? -> t['#']가 없는 경우가 있다.
        if '#' in t:
            return True
        # 'hello#'만 들어가 있는데, 여기서 False를 안해주면 'hell'도 있는 단어가 된다.
        return False

    def startsWith(self, prefix):
        t = self.link
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

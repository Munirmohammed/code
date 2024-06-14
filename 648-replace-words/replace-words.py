class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split()
        for i in range(len(words)):
            node = trie.root
            for j in range(len(words[i])):
                if words[i][j] not in node.children:
                    break
                node = node.children[words[i][j]]
                if node.isEnd:
                    words[i] = words[i][:j+1]
                    break

        return ' '.join(words)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build Trie from dictionary
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.endOfWord = True

        # Replace words in sentence
        words = sentence.split()
        for i in range(len(words)):
            node = root
            for j in range(len(words[i])):
                if words[i][j] in node.children:
                    node = node.children[words[i][j]]
                    if node.endOfWord:
                        words[i] = words[i][:j+1]
                        break
                else:
                    break

        return ' '.join(words)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
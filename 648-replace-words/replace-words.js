class TrieNode {
    constructor() {
        this.children = {};
        this.isEnd = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (let ch of word) {
            if (!node.children[ch]) {
                node.children[ch] = new TrieNode();
            }
            node = node.children[ch];
        }
        node.isEnd = true;
    }
}

var replaceWords = function(dictionary, sentence) {
    const trie = new Trie();
    for (let word of dictionary) {
        trie.insert(word);
    }

    const words = sentence.split(' ');
    for (let i = 0; i < words.length; i++) {
        let node = trie.root;
        for (let j = 0; j < words[i].length; j++) {
            if (!node.children[words[i][j]]) {
                break;
            }
            node = node.children[words[i][j]];
            if (node.isEnd) {
                words[i] = words[i].substring(0, j + 1);
                break;
            }
        }
    }

    return words.join(' ');
};
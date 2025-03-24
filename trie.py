class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Stores the complete word for suggestions

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def _predict_helper(self, node, suggestions):
        if node.is_end_of_word:
            suggestions.append(node.word)
        for child in node.children.values():
            self._predict_helper(child, suggestions)

    def predict(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No words with this prefix
            node = node.children[char]

        suggestions = []
        self._predict_helper(node, suggestions)
        return suggestions

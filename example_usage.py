from trie import Trie

# Initialize Trie
trie = Trie()

# Load words from dataset.txt (assuming each word is on a new line)
with open("dataset.txt", "r") as file:
    words = file.read().splitlines()

# Insert words into Trie
for word in words:
    trie.insert(word)

# Searching for words
print("Search Results:")
print("help ->", trie.search("help"))
print("hero ->", trie.search("hero"))
print("hell ->", trie.search("hell"))
print("unknown ->", trie.search("unknown"))

# Predictive text suggestions
print("\nPredictions:")
print("hel ->", trie.predict("hel"))
print("he ->", trie.predict("he"))
print("hea ->", trie.predict("hea"))

Let's break down the **time complexity analysis step-by-step** for each operation in the **Trie algorithm** using **Master's Theorem** where applicable.

---

## **1. Insertion Complexity**
### **Steps in the `insert` function**
```python
def insert(self, word):
    node = self.root  # O(1)
    for char in word:  # O(m), where m is the length of the word
        if char not in node.children:  # O(1) lookup in dictionary
            node.children[char] = TrieNode()  # O(1) new node creation
        node = node.children[char]  # O(1) traversal
    node.is_end_of_word = True  # O(1)
    node.word = word  # O(1)
```

### **Total Complexity for Insertion**
- Loop runs for **m** characters.
- Each iteration does **O(1)** work.
- **Total Complexity:** **O(m)**

---

## **2. Search Complexity**
### **Steps in the `search` function**
```python
def search(self, word):
    node = self.root  # O(1)
    for char in word:  # O(m), where m is the length of the word
        if char not in node.children:  # O(1) lookup
            return False  # O(1)
        node = node.children[char]  # O(1) traversal
    return node.is_end_of_word  # O(1)
```

### **Total Complexity for Search**
- Similar to insertion, the loop runs for **m** characters.
- Each iteration takes **O(1)** time.
- **Total Complexity:** **O(m)**

---

## **3. Prediction Complexity**
### **Steps in the `predict` function**
```python
def predict(self, prefix):
    node = self.root  # O(1)
    for char in prefix:  # O(p), where p is the length of the prefix
        if char not in node.children:  # O(1) lookup
            return []  # O(1)
        node = node.children[char]  # O(1) traversal
    
    suggestions = []  # O(1)
    self._predict_helper(node, suggestions)  # Recursive call
    return suggestions  # O(1)
```

### **Recursive `_predict_helper` Function**
```python
def _predict_helper(self, node, suggestions):
    if node.is_end_of_word:  # O(1)
        suggestions.append(node.word)  # O(1)
    for char, child_node in node.children.items():  # O(Σ), where Σ is the alphabet size (26 for English)
        self._predict_helper(child_node, suggestions)  # Recursive calls
```

### **Recurrence Relation for `_predict_helper`**
Since each node calls itself recursively for each child:

\[
T(n) = cT(n/c) + O(1)
\]

Using **Master’s Theorem**:

- \( a = c \) (number of recursive calls per node)
- \( b = c \) (each call processes one branch)
- \( f(n) = O(1) \) (constant work per node)

Since \( \log_c(c) = 1 \), and \( O(1) \) is smaller than \( O(n^1) \), we apply **Case 1**:

\[
T(n) = O(n)
\]

Thus, **time complexity of `predict` is O(k) where k is the number of matching words**.

---

## **Final Complexity Analysis**
| **Operation** | **Time Complexity** |
|--------------|--------------------|
| **Insertion** | **O(m)** |
| **Search** | **O(m)** |
| **Prediction** | **O(p + k)** (where \( p \) is prefix length and \( k \) is the number of suggestions) |

### **Best, Average, and Worst Case Complexity**
| Case | Insertion | Search | Prediction |
|------|-----------|--------|------------|
| **Best Case** | **O(1)** (if prefix exists) | **O(1)** (if found early) | **O(1)** (few matches) |
| **Average Case** | **O(m)** | **O(m)** | **O(p + k)** |
| **Worst Case** | **O(m)** | **O(m)** | **O(n)** (if all words match) |

---

## **Conclusion**
1. **Insertion & Search** take **O(m)**, making Trie efficient for lookups.
2. **Prediction** takes **O(p + k)**, which is better than scanning a full dictionary.
3. **Trie improves upon traditional linear searches in dictionaries** by reducing lookup time **from O(n) to O(m)**.

Would you like a space complexity breakdown too? 🚀

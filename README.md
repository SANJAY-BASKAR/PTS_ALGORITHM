# Trie-Based Predictive Search Algorithm

## 📌 Overview
This project implements an **optimized Trie data structure** for predictive search. It enhances traditional Trie search by incorporating **path compression, frequency-based ranking, and efficient memory usage**, making word predictions faster and more accurate.

## 🔍 Features
- **Fast Word Insertion & Lookup**: Efficiently stores and retrieves words in **O(m)** time.
- **Predictive Search**: Suggests words based on prefixes, improving typing efficiency.
- **Optimized Memory Usage**: Reduces space complexity using **path compression**.
- **Frequency-Based Ranking**: Ranks predictions based on word usage frequency.
- **Efficient Search Time**: Enhances traditional search using ranked retrieval.

## 📂 File Structure
```
📁 Trie_Predictive_Search
 ├── 📜 trie.py               # Implementation of Trie Algorithm
 ├── 📜 dataset.txt           # SCOWL dataset (word list)
 ├── 📜 example_usage.py      # Demonstration script
 ├── 📜 README.md             # Project Documentation (This file)
 └── 📜 results.png           # Graphs comparing performance
```

## 🚀 Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Trie-Predictive-Search.git
cd Trie-Predictive-Search
```

### 2️⃣ Run the Example
```bash
python example_usage.py
```

## 🛠 Implementation Details
### **1️⃣ Trie Node & Structure**
- Each node contains **children pointers**, an **end-of-word flag**, and an **optional word reference**.
- Uses **path compression** to optimize storage.

### **2️⃣ Word Insertion (O(m))**
- Inserts each character as a child node.
- Marks the end of a word with a flag.

### **3️⃣ Word Search (O(m))**
- Traverses characters in sequence to check if a word exists.

### **4️⃣ Predictive Search (O(k))**
- Searches for a given prefix.
- Retrieves **top-k suggestions** ranked by frequency.

## 📊 Performance Analysis
### **Time Complexity**
| Operation      | Complexity |
|---------------|------------|
| Insertion     | O(m)       |
| Search        | O(m)       |
| Prediction    | O(k)       |

### **Memory Usage Comparison**
✅ **Optimized Trie** uses **less memory** compared to a standard Trie.

## 📸 Visual Representation
![Performance Graph](results.png)
- **Red Line**: Optimized Trie (Faster & Less Memory Usage)
- **Blue Line**: Traditional Trie

## 📜 References
- SCOWL Dataset: [Link](http://wordlist.aspell.net/)
- Research Paper: **Efficient Trie-Based Search Optimization**

## 📬 Contact
For any queries, feel free to reach out!
📧 Email: sanjaybaskar.in@gmail.com 
🔗 GitHub: [SANJAY BASKAR](https://github.com/SANJAY-BASKAR)


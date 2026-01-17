# Implement Trie (Prefix Tree) - leetcode - 208


from typing import Any


class Trie:
    def __init__(self):
        self.children = dict[str, Any]()
        self.is_end = False

    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.is_end:
            return True
        else:
            return False

    def startsWith(self, word):
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True


t1 = Trie()
t1.insert("apple")
# t1.insert("app")

# print(t1.search("apple"))  # Should be True
# print(t1.search("app"))  # Should be True
# print(t1.search("appl"))  # Should be False (not a complete word)
# print(t1.startsWith("app"))  # Should be True
# print(t1.startsWith("ap"))  # Should be True
# print(t1.startsWith("b"))  # Should be False

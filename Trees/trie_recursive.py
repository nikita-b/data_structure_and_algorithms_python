class TrieNode:
    def __init__(self, end: bool = False):
        self.children = {}
        self.end = end

    def add_child(self, key, node):
        self.children[key] = node

    def get_child(self):
        return self.children

    def is_end(self): # Real drama!
        return self.end


class Trie:
    def __init__(self):
        """
        Create root node
        """
        self.trie = TrieNode()
        self.current = self.trie

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.trie

        for i in word:
            if i not in current_node.get_child():
                new_node = TrieNode()
                current_node.add_child(i, new_node)
            current_node = current_node.get_child()[i]
        current_node.end = True

    def recursion(self, word: str, starts_with: bool = False) -> bool:
        if not word and (starts_with or self.current.is_end()):
            return True

        if not word:
            return False

        current_char = word[0]

        if current_char in self.current.get_child():
            self.current = self.current.get_child()[current_char]
            return self.recursion(word[1:], starts_with)

        return False

    def search(self, word: str, starts_with: bool = False) -> bool:
        """
        Returns True if the word is in the trie and False otherwise
        """
        self.current = self.trie

        return self.recursion(word, starts_with)

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        return self.search(prefix, True)

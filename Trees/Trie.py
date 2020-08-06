class TrieNode:
    def __init__(self, end: bool = False):
        self.children = {}
        self.end = end

    def add_child(self, key, node):
        self.children[key] = node

    def get_links(self):
        return self.children

    def is_end(self): # Real drama!
        return self.end


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.trie

        for i in word:
            if i not in current_node.get_links():
                new_node = TrieNode(None)
                current_node.add_child(i, new_node)
            current_node = current_node.get_links()[i]
        current_node.end = True

    def search(self, word: str, start_with: bool = False) -> bool:
        """
        Returns True if the word is in the trie and False otherwise
        """
        current_node = self.trie

        for i in word:
            if i in current_node.get_links():
                current_node = current_node.children[i]
                continue
            return False

        if not start_with and not current_node.is_end():
            return False

        return True

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        return self.search(prefix, True)

"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

from string import ascii_lowercase


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = [None] * len(ascii_lowercase)
        self.end = False

    def insert(self, word):
        cur = self
        for ch in word:
            index = ord(ch) - ord("a")
            if cur.children[index] is not None:
                cur = cur.children[index]
                continue

            node = Node(ch)
            cur.children[index] = node
            cur = node
        cur.end = True

    def search(self, prefix) -> bool:
        cur = self
        for ch in prefix:
            index = ord(ch) - ord("a")
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return cur.end

    def check_prefix(self, prefix) -> bool:
        cur = self
        for ch in prefix:
            index = ord(ch) - ord("a")
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return True


class Trie:
    def __init__(self):
        self.trie = Node("")

    def insert(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)

    def startsWith(self, prefix: str) -> bool:
        return self.trie.check_prefix(prefix)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("cat")
    assert trie.search("apple")
    assert not trie.search("app")
    assert not trie.search("a")
    assert trie.startsWith("app")

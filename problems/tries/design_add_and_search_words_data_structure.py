"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 3 dots in word for search queries.
    At most 104 calls will be made to addWord and search.
"""

from string import ascii_lowercase


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = [None] * len(ascii_lowercase)
        self.end = False

    def __str__(self) -> str:
        children = ",".join([x[0].val for x in self.children if x is not None])
        return f"Node: {self.val} {self.end} {children}"

    def insert(self, word):
        cur = self
        for n, ch in enumerate(word):
            i = ord(ch) - ord("a")
            if cur.children[i] is not None:
                child, size = cur.children[i]
                cur.children[i] = (child, max(size, len(word[n:])))
                cur = child
                continue

            node = Node(ch)
            cur.children[i] = (node, len(word[n:]))
            cur = node

        cur.end = True

    def search(self, word):
        cur = self
        for n, ch in enumerate(word):
            if ch != ".":
                i = ord(ch) - ord("a")
                if cur.children[i] is None:
                    return False
                cur, _ = cur.children[i]
            else:
                children = (x for x in cur.children if x is not None)
                for child, size in children:
                    if size < len(word[n:]):
                        continue
                    if child.search(word[n + 1 :]):
                        return True
                return False
        return cur.end


class WordDictionary:
    def __init__(self):
        self.trie = Node("")
        self.cache = {}

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        self.cache = {}

    def search(self, word: str) -> bool:
        result = self.trie.search(word)
        self.cache[word] = result
        return result


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("ab")
    cases = [
        ["a"],
        ["a."],
        ["ab"],
        [".a"],
        [".b"],
        ["ab."],
        ["."],
        [".."],
    ]
    ans = [True, True, True, False, True, False, True, True]
    for i in range(len(cases)):
        assert wd.search(cases[i][0]) == ans[i]

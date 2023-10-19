class TrieNode: 
    def __init__(self): 
        self.children = [None for _ in range(26)]
        self.endWord = False
​
​
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
​
​
    def addWord(self, word: str) -> None:
        curr = self.root
        for chx in word:
            if curr.children[ord(chx) - ord('a') ] == None:
                curr.children[ord(chx) - ord('a') ] = TrieNode()
            curr = curr.children[ord(chx) - ord('a') ]
        curr.endWord = True
​
​
    def search(self, word: str) -> bool:
       
        def recurse(idx, root):
            print
            if idx == len(word):
                return root.endWord 
​
            chx = word[idx]
            if chx == ".":

class TrieNode :
    def __init__(self):
        self.children = {}
        self.sum = 0
        
class MapSum:
​
    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)
​
    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        curr = self.root
        self.map[key] = val     
        for w in key:
            if w not in curr.children:
                curr.children[w] = TrieNode()
                
            curr = curr.children[w]
            curr.sum += diff
            
​
    def sum(self, prefix: str) -> int:
        curr = self.root 
        # print(curr.children)
        for w in prefix:
            if w not in curr.children:
                # curr.children[w] = TrieNode()
                return 0
